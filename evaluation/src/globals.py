import os

class Globals:
    ROOT_PATH = os.path.abspath("../../")   # your absolute root path
    DATASET_PATH = os.path.join(ROOT_PATH, "benchmark")
    METADATA_PATH = os.path.join(ROOT_PATH, "metadata.json")
    RESULT_PATH = os.path.join(ROOT_PATH, "evaluation", "results")
