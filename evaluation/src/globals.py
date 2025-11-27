import os

class Globals:
    ROOT_PATH = os.path.abspath("../../")
    DATASET_PATH = os.path.join(ROOT_PATH, "benchmark")
    METADATA_PATH = os.path.join(DATASET_PATH, "metadata.json")
    RESULT_PATH = os.path.join(ROOT_PATH, "evaluation", "results")
