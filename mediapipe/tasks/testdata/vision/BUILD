# Copyright 2022 The MediaPipe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

load(
    "//mediapipe/framework/tool:mediapipe_files.bzl",
    "mediapipe_files",
)

package(
    default_visibility = ["//mediapipe/tasks:internal"],
    licenses = ["notice"],  # Apache 2.0
)

mediapipe_files(srcs = [
    "burger.jpg",
    "burger_crop.jpg",
    "burger_rotated.jpg",
    "cat.jpg",
    "cat_mask.jpg",
    "cats_and_dogs.jpg",
    "cats_and_dogs_no_resizing.jpg",
    "cats_and_dogs_rotated.jpg",
    "coco_efficientdet_lite0_v1_1.0_quant_2021_09_06.tflite",
    "coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.tflite",
    "coco_ssd_mobilenet_v1_1.0_quant_2018_06_29_with_dummy_score_calibration.tflite",
    "deeplabv3.tflite",
    "hand_landmark.task",
    "hand_landmark_full.tflite",
    "hand_landmark_lite.tflite",
    "left_hands.jpg",
    "left_hands_rotated.jpg",
    "mobilenet_v1_0.25_192_quantized_1_default_1.tflite",
    "mobilenet_v1_0.25_224_1_default_1.tflite",
    "mobilenet_v1_0.25_224_1_metadata_1.tflite",
    "mobilenet_v1_0.25_224_quant.tflite",
    "mobilenet_v1_0.25_224_quant_with_dummy_score_calibration.tflite",
    "mobilenet_v1_0.25_224_quant_without_subgraph_metadata.tflite",
    "mobilenet_v2_1.0_224.tflite",
    "mobilenet_v3_small_100_224_embedder.tflite",
    "mozart_square.jpg",
    "multi_objects.jpg",
    "multi_objects_rotated.jpg",
    "palm_detection_full.tflite",
    "pointing_up.jpg",
    "pointing_up_rotated.jpg",
    "right_hands.jpg",
    "right_hands_rotated.jpg",
    "segmentation_golden_rotation0.png",
    "segmentation_input_rotation0.jpg",
    "selfie_segm_128_128_3.tflite",
    "selfie_segm_128_128_3_expected_mask.jpg",
    "selfie_segm_144_256_3.tflite",
    "selfie_segm_144_256_3_expected_mask.jpg",
    "thumb_up.jpg",
])

exports_files(
    srcs = [
        "expected_left_down_hand_landmarks.prototxt",
        "expected_left_down_hand_rotated_landmarks.prototxt",
        "expected_left_up_hand_landmarks.prototxt",
        "expected_left_up_hand_rotated_landmarks.prototxt",
        "expected_right_down_hand_landmarks.prototxt",
        "expected_right_up_hand_landmarks.prototxt",
    ],
)

filegroup(
    name = "test_images",
    srcs = [
        "burger.jpg",
        "burger_crop.jpg",
        "burger_rotated.jpg",
        "cat.jpg",
        "cat_mask.jpg",
        "cats_and_dogs.jpg",
        "cats_and_dogs_no_resizing.jpg",
        "cats_and_dogs_rotated.jpg",
        "hand_landmark_full.tflite",
        "hand_landmark_lite.tflite",
        "left_hands.jpg",
        "left_hands_rotated.jpg",
        "mozart_square.jpg",
        "multi_objects.jpg",
        "multi_objects_rotated.jpg",
        "pointing_up.jpg",
        "pointing_up_rotated.jpg",
        "right_hands.jpg",
        "right_hands_rotated.jpg",
        "segmentation_golden_rotation0.png",
        "segmentation_input_rotation0.jpg",
        "selfie_segm_128_128_3_expected_mask.jpg",
        "selfie_segm_144_256_3_expected_mask.jpg",
        "thumb_up.jpg",
    ],
    visibility = [
        "//mediapipe/python:__subpackages__",
        "//mediapipe/tasks:internal",
    ],
)

# TODO Create individual filegroup for models required for each Tasks.
filegroup(
    name = "test_models",
    srcs = [
        "coco_efficientdet_lite0_v1_1.0_quant_2021_09_06.tflite",
        "coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.tflite",
        "coco_ssd_mobilenet_v1_1.0_quant_2018_06_29_with_dummy_score_calibration.tflite",
        "deeplabv3.tflite",
        "hand_landmark.task",
        "hand_landmark_full.tflite",
        "hand_landmark_lite.tflite",
        "mobilenet_v1_0.25_192_quantized_1_default_1.tflite",
        "mobilenet_v1_0.25_224_1_default_1.tflite",
        "mobilenet_v1_0.25_224_1_metadata_1.tflite",
        "mobilenet_v1_0.25_224_quant.tflite",
        "mobilenet_v1_0.25_224_quant_with_dummy_score_calibration.tflite",
        "mobilenet_v1_0.25_224_quant_without_subgraph_metadata.tflite",
        "mobilenet_v2_1.0_224.tflite",
        "mobilenet_v3_small_100_224_embedder.tflite",
        "palm_detection_full.tflite",
        "selfie_segm_128_128_3.tflite",
        "selfie_segm_144_256_3.tflite",
    ],
)

filegroup(
    name = "test_protos",
    srcs = [
        "expected_left_down_hand_landmarks.prototxt",
        "expected_left_down_hand_rotated_landmarks.prototxt",
        "expected_left_up_hand_landmarks.prototxt",
        "expected_left_up_hand_rotated_landmarks.prototxt",
        "expected_right_down_hand_landmarks.prototxt",
        "expected_right_up_hand_landmarks.prototxt",
        "hand_detector_result_one_hand.pbtxt",
        "hand_detector_result_one_hand_rotated.pbtxt",
        "hand_detector_result_two_hands.pbtxt",
        "pointing_up_landmarks.pbtxt",
        "pointing_up_rotated_landmarks.pbtxt",
        "thumb_up_landmarks.pbtxt",
        "thumb_up_rotated_landmarks.pbtxt",
    ],
)
