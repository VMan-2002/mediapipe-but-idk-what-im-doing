# Placeholder for internal Python strict test compatibility macro.

package(
    default_visibility = [
        "//visibility:public",
    ],
    licenses = ["notice"],  # Apache 2.0
)

py_test(
    name = "metadata_info_test",
    srcs = ["metadata_info_test.py"],
    data = [
        "//mediapipe/tasks/testdata/metadata:data_files",
    ],
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        "//mediapipe/tasks/metadata:metadata_schema_py",
        "//mediapipe/tasks/metadata:schema_py",
        "//mediapipe/tasks/python/metadata",
        "//mediapipe/tasks/python/metadata/metadata_writers:metadata_info",
        "//mediapipe/tasks/python/test:test_utils",
        "@flatbuffers//:runtime_py",
    ],
)

py_test(
    name = "metadata_writer_test",
    srcs = ["metadata_writer_test.py"],
    data = ["//mediapipe/tasks/testdata/metadata:model_files"],
    deps = [
        "//mediapipe/tasks/python/metadata/metadata_writers:metadata_writer",
        "//mediapipe/tasks/python/test:test_utils",
    ],
)
