#!/bin/bash

# =======================================================
# Python Venv Restoration Helper
# Action: Create 'venv' and install from ../requirements.txt
# =======================================================

# Configuration
CONDA_ENV="adapteval"
VENV_NAME="venv"
INPUT_FILE="../requirements.txt"


# 1. Check if requirements file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Requirements file not found at '$INPUT_FILE'"
    exit 1
fi

echo "Input file found: $INPUT_FILE"
echo "Looking for Conda environment: $CONDA_ENV..."

# Get the path of the conda environment
CONDA_ENV_PATH=$(conda env list | grep -E "^$CONDA_ENV\s" | awk '{print $NF}')

# Handle the case where the env is currently active (marked with *)
if [ -z "$CONDA_ENV_PATH" ]; then
    # Try pattern with star
    CONDA_ENV_PATH=$(conda env list | grep -E "^$CONDA_ENV\s+\*" | awk '{print $NF}')
fi


if [ -z "$CONDA_ENV_PATH" ]; then
    echo "Error: Could not find a Conda environment named '$CONDA_ENV'."
    echo "Available environments:"
    conda env list
    exit 1
fi

# Construct the full path to python executable
TARGET_PYTHON="$CONDA_ENV_PATH/bin/python"
echo "Target Python path: $TARGET_PYTHON; Version: $($TARGET_PYTHON --version))"

echo "Creating virtual environment '$VENV_NAME'..."

# 2. Create the virtual environment
"$TARGET_PYTHON" -m venv "$VENV_NAME"

if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment."
    exit 1
fi

# 3. Activate, Upgrade Pip, and Install Dependencies
(
    source "$VENV_NAME/bin/activate"

    echo "Environment activated. Upgrading pip..."
    # Always a good practice to upgrade pip first
    python -m pip install --upgrade pip

    echo "Installing dependencies..."
    python -m pip install -r "$INPUT_FILE"


    if [ $? -eq 0 ]; then
        echo "---------------------------------------------------"
        echo "Success! Environment created and packages installed."
        echo "To use it, run: source $VENV_NAME/bin/activate"
        echo "---------------------------------------------------"
    else
        echo "Error: Failed to install dependencies."
        exit 1
    fi
)
