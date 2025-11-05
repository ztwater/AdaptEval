# AdaptEval: A Benchmark for Evaluating Large Language Models on Code Snippet Adaptation

AdaptEval is a benchmark for evaluating LLMs on code snippet adaptation tasks. It includes 164 tasks with 523 adaptations in Python language. It incorporates three distinctive features: (1) **Practical Context** from developers real-world code adaptation practices from Stack Overflow (SO) to GitHub; (2) **Multi-granularity Annotation** including task-level and adaptation-level requirements restored by manual annotation; (3) **Fine-grained Evaluation** to assess LLMs' performance across individual adaptations. Each task contains an average of 3.2 adaptations, 4.0 dependencies and 6.6 test cases.

## Overall structure

![Overall Structure of AdaptEval](./figures/overview.pdf "Overall Structure of AdaptEval")

## Directory

```
AdaptEval/
├─ metadata.json
├─ benchmark/
│  ├─ REPO_ID/
│  │  ├─ dataset_items/
│  │  │  ├─ {LINKED_SO_SNIPPET}.py
│  │  │  ├─ {ADAPTED_FILE}.py
│  │  │  ├─ adaptation_task_for_{METHOD_NAME}/
│  │  │  │  ├─ task_description.txt
│  │  │  │  ├─ annotated_adaptations.txt
│  │  │  ├─ test_{ADAPTED_FILE}_{METHOD_NAME}.py
│  │  │  ├─ linked_posts/
│  │  ├─ {GITHUB_REPO_NAME}/
│  │  │  ├─ venv/
│  │  │  ├─ tests/
│  │  │  │  ├─ test_adapteval/
│  ├─ .../
├─ evaluation/
│  ├─ prompts/
│  ├─ src/
│  ├─ results/
├─ obfuscated-version/
│  ├─ TASK_NAMESPACE/
│  │  ├─ original_code.py
│  │  ├─ obfuscated_code.py
│  │  ├─ deobfuscated_map.json
│  │  ├─ ast.txt
├─ figures/
├─ README.md
```

`metadata.json` includes all metadata of our tasks, contexts and annotations. You can traverse this file to obtain task requirements, related SO posts and GitHub projects, etc.

All repositories in ***AdaptEval*** are included in the `benchmark/` folder. Each repository is associated with an integer index `REPO_ID` and a corresponding folder. The repository folder contains two subfolders, i.e., `dataset_items/` and `{GITHUB_REPO_NAME}`.

The first folder `dataset_items/` includes all materials we have created during benchmark construction, as shown in the following:
1. Reused Snippet: the reused SO code, whose name is `35804945_0.py` the first consecutive numbers is the answer id of the SO post. You can access it by visiting `stackoverflow.com/a/35804945`.
2. Adapted Snippet: the adapted function in the GitHub project. We extract the target function from the original file for your convenience, whose name is the original file name in the GitHub project (maybe with an additional prefix `ctx_` for the identification purpose).
3. Adaptation Task: all the annotations for each adaptation task is provided, with a text file `task_description.txt` describing our task-level description, and an `annotated_adaptations.txt` file to record the adaptation type, adaptation-level description and dependencies for each adaptation.
4. Test Suite: all the task-level and adaptation-level tests, whose file name has a prefix `test_`.
5. Linked Posts: all the SO posts referenced by the target GitHub code file. We also retain the extracted code snippets from answer posts. These are located in the `linked_posts/` folder, 

After downloading our complete GitHub repositories, you can unzip them in their corresponding directories (`benchmark/{REPO_ID}`). `GITHUB_REPO_NAME` stands for the original GitHub repository name. This is the second folder. We have pre-install the requirments in the `venv/` folder and included the tests in the `tests/test_adapteval/` folder.

`evaluation` repository is our replication package for evaluation, where `prompts` directory places our prompts for all settings available in AdaptEval.

`obfuscated-version/` repository provides the mutated code for data leakage evaluation and mitigation, which contains the abstract syntax tree of the reused snippet, its original version, its obfuscated version and a json file `deobfuscated_map.json` to restore the identifier names of LLM-generated code for test execution.

`figures` directory includes illustrative figures for AdaptEval.

## Installation

1. Environmental Setup

```shell
# create a new environment, i.e., conda
$ conda create -n adapteval python=3.11
$ conda activate 

# update all virtual environment variables
$ cd evaluation/src
$ python set_env.py --python_home /home/user/anaconda3/bin --python_version 3.11.7 --dataset_root /home/user/AdaptEval
```

2. Install Requirement For Evaluation

Run the following command to install required dependencies

```shell
$ pip install -r requirements.txt
```

3. Data Downloading

Due to the size of collected repositories, we upload it to [link](). Please first download it and unzip to the `benchmark/` directory.

``` shell
$ tar -xzf data.tar.gz --strip-components=1 -C benchmark
```

---

## Run Evaluation

```bash
cd evaluation/src

python run.py --inference True --test True --model_str gpt-4o --task_mode 0 --dep_mode Oracle --temperature 0.2 --repeat 5
```

- `inference` and `test` parameters aim for running inference or test only.

- `model_str` specifies the model used as it appears in the chat completion api, including gpt series, deepseek series, etc.
- `task_mode` specifies the requirement specificity, `0` for adaptation-level (**AReq**), `1` for task-level (**TReq**), and `2` for (**NoReq**).
- `dep_mode` specifies whether code references are included, the valid choices are `None` and `Oracle` now.
- `temperature` is the model temperature and `repeat` means the repeat time of the sampling.

You can find the results in `evaluation/results` folder.

---
