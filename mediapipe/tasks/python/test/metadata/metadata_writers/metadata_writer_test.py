# Copyright 2022 The MediaPipe Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for metadata writer classes."""
from absl.testing import absltest

from mediapipe.tasks.python.metadata.metadata_writers import metadata_writer
from mediapipe.tasks.python.test import test_utils

_IMAGE_CLASSIFIER_MODEL = test_utils.get_test_data_path(
    'mobilenet_v1_0.25_224_1_default_1.tflite')


class LabelsTest(absltest.TestCase):

  def test_category_name(self):
    labels = metadata_writer.Labels()
    self.assertEqual(
        labels.add(['a', 'b'])._labels, [
            metadata_writer.LabelItem(
                filename='labels.txt', names=['a', 'b'], locale=None)
        ])

  def test_locale(self):
    labels = metadata_writer.Labels()

    # Add from file.
    en_filepath = self.create_tempfile().full_path
    with open(en_filepath, 'w') as f:
      f.write('a\nb')
    labels.add_from_file(en_filepath, 'en')

    # Customized file name.
    labels.add(['A', 'B'], 'fr', exported_filename='my_file.txt')
    self.assertEqual(labels._labels, [
        metadata_writer.LabelItem('labels_en.txt', ['a', 'b'], 'en'),
        metadata_writer.LabelItem('my_file.txt', ['A', 'B'], 'fr'),
    ])


class MetadataWriterForTaskTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    with open(_IMAGE_CLASSIFIER_MODEL, 'rb') as f:
      self.image_classifier_model_buffer = f.read()

  def test_initialize_and_populate(self):
    writer = metadata_writer.MetadataWriter.create(
        self.image_classifier_model_buffer)
    writer.add_genernal_info(
        model_name='my_image_model', model_description='my_description')
    tflite_model, metadata_json = writer.populate()
    self.assertLen(tflite_model, 1882986)
    self.assertJsonEqual(
        metadata_json, """{
          "name": "my_image_model",
          "description": "my_description",
          "subgraph_metadata": [
            {
              "input_tensor_metadata": [
                {
                  "name": "input"
                }
              ],
              "output_tensor_metadata": [
                {
                  "name": "MobilenetV1/Predictions/Reshape_1"
                }
              ]
            }
          ],
          "min_parser_version": "1.0.0"
        }
        """)

  def test_add_feature_input_output(self):
    writer = metadata_writer.MetadataWriter.create(
        self.image_classifier_model_buffer)
    writer.add_genernal_info(
        model_name='my_model', model_description='my_description')
    writer.add_feature_input(
        name='input_tesnor', description='a feature input tensor')
    writer.add_feature_output(
        name='output_tesnor', description='a feature output tensor')

    _, metadata_json = writer.populate()
    self.assertJsonEqual(
        metadata_json, """{
          "name": "my_model",
          "description": "my_description",
          "subgraph_metadata": [
            {
              "input_tensor_metadata": [
                {
                  "name": "input_tesnor",
                  "description": "a feature input tensor",
                  "content": {
                    "content_properties_type": "FeatureProperties",
                    "content_properties": {
                    }
                  },
                  "stats": {
                  }
                }
              ],
              "output_tensor_metadata": [
                {
                  "name": "output_tesnor",
                  "description": "a feature output tensor",
                  "content": {
                    "content_properties_type": "FeatureProperties",
                    "content_properties": {
                    }
                  },
                  "stats": {
                  }
                }
              ]
            }
          ],
          "min_parser_version": "1.0.0"
        }
        """)

  def test_image_classifier(self):
    writer = metadata_writer.MetadataWriter.create(
        self.image_classifier_model_buffer)
    writer.add_genernal_info(
        model_name='image_classifier',
        model_description='Imagenet classification model')
    writer.add_image_input(
        norm_mean=[127.5, 127.5, 127.5],
        norm_std=[127.5, 127.5, 127.5],
        color_space_type=metadata_writer.MetadataWriter.color_space_types.RGB)
    writer.add_classification_output(metadata_writer.Labels().add(
        ['a', 'b', 'c']))
    _, metadata_json = writer.populate()
    self.assertJsonEqual(
        metadata_json, """{
          "name": "image_classifier",
          "description": "Imagenet classification model",
          "subgraph_metadata": [
            {
              "input_tensor_metadata": [
                {
                  "name": "image",
                  "description": "Input image to be processed.",
                  "content": {
                    "content_properties_type": "ImageProperties",
                    "content_properties": {
                      "color_space": "RGB"
                    }
                  },
                  "process_units": [
                    {
                      "options_type": "NormalizationOptions",
                      "options": {
                        "mean": [
                          127.5,
                          127.5,
                          127.5
                        ],
                        "std": [
                          127.5,
                          127.5,
                          127.5
                        ]
                      }
                    }
                  ],
                  "stats": {
                    "max": [
                      1.0,
                      1.0,
                      1.0
                    ],
                    "min": [
                      -1.0,
                      -1.0,
                      -1.0
                    ]
                  }
                }
              ],
              "output_tensor_metadata": [
                {
                  "name": "score",
                  "description": "Score of the labels respectively",
                  "content": {
                    "content_properties_type": "FeatureProperties",
                    "content_properties": {
                    }
                  },
                  "stats": {
                    "max": [
                      1.0
                    ],
                    "min": [
                      0.0
                    ]
                  },
                  "associated_files": [
                    {
                      "name": "labels.txt",
                      "description": "Labels for categories that the model can recognize.",
                      "type": "TENSOR_AXIS_LABELS"
                    }
                  ]
                }
              ]
            }
          ],
          "min_parser_version": "1.0.0"
        }
        """)

  def test_image_classifier_with_locale_and_score_calibration(self):
    writer = metadata_writer.MetadataWriter(self.image_classifier_model_buffer)
    writer.add_genernal_info(
        model_name='image_classifier',
        model_description='Classify the input image.')
    writer.add_image_input(
        norm_mean=[127.5, 127.5, 127.5],
        norm_std=[127.5, 127.5, 127.5],
        color_space_type=metadata_writer.MetadataWriter.color_space_types.RGB)
    writer.add_classification_output(
        metadata_writer.Labels().add(['/id1',
                                      '/id2']).add(['tulip', 'lily'],
                                                   'en').add(['tulipe', 'lis'],
                                                             'fr'),
        score_calibration=metadata_writer.ScoreCalibration(
            metadata_writer.ScoreCalibration.transformation_types
            .INVERSE_LOGISTIC, [
                metadata_writer.CalibrationParameter(1., 2., 3., None),
                metadata_writer.CalibrationParameter(1., 2., 3., 4.),
            ],
            default_score=0.5))
    _, metadata_json = writer.populate()
    self.assertJsonEqual(
        metadata_json, """{
          "name": "image_classifier",
          "description": "Classify the input image.",
          "subgraph_metadata": [
            {
              "input_tensor_metadata": [
                {
                  "name": "image",
                  "description": "Input image to be processed.",
                  "content": {
                    "content_properties_type": "ImageProperties",
                    "content_properties": {
                      "color_space": "RGB"
                    }
                  },
                  "process_units": [
                    {
                      "options_type": "NormalizationOptions",
                      "options": {
                        "mean": [
                          127.5,
                          127.5,
                          127.5
                        ],
                        "std": [
                          127.5,
                          127.5,
                          127.5
                        ]
                      }
                    }
                  ],
                  "stats": {
                    "max": [
                      1.0,
                      1.0,
                      1.0
                    ],
                    "min": [
                      -1.0,
                      -1.0,
                      -1.0
                    ]
                  }
                }
              ],
              "output_tensor_metadata": [
                {
                  "name": "score",
                  "description": "Score of the labels respectively",
                  "content": {
                    "content_properties_type": "FeatureProperties",
                    "content_properties": {
                    }
                  },
                  "process_units": [
                    {
                      "options_type": "ScoreCalibrationOptions",
                      "options": {
                        "score_transformation": "INVERSE_LOGISTIC",
                        "default_score": 0.5
                      }
                    }
                  ],
                  "stats": {
                    "max": [
                      1.0
                    ],
                    "min": [
                      0.0
                    ]
                  },
                  "associated_files": [
                    {
                      "name": "labels.txt",
                      "description": "Labels for categories that the model can recognize.",
                      "type": "TENSOR_AXIS_LABELS"
                    },
                    {
                      "name": "labels_en.txt",
                      "description": "Labels for categories that the model can recognize.",
                      "type": "TENSOR_AXIS_LABELS",
                      "locale": "en"
                    },
                    {
                      "name": "labels_fr.txt",
                      "description": "Labels for categories that the model can recognize.",
                      "type": "TENSOR_AXIS_LABELS",
                      "locale": "fr"
                    },
                    {
                      "name": "score_calibration.txt",
                      "description": "Contains sigmoid-based score calibration parameters. The main purposes of score calibration is to make scores across classes comparable, so that a common threshold can be used for all output classes.",
                      "type": "TENSOR_AXIS_SCORE_CALIBRATION"
                    }
                  ]
                }
              ]
            }
          ],
          "min_parser_version": "1.0.0"
        }
        """)


if __name__ == '__main__':
  absltest.main()
