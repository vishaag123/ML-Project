import os
from pathlib import Path
import logging

# Configure logging for informative output
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

# Project name to be used in file paths
project_name = "CNNClassifier"

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",  # Empty file for GitHub workflows folder
    f"src/{project_name}/__init__.py",  # Initialization file for project directory
    f"src/{project_name}/components/__init__.py",  # Initialization file for components subdirectory
    f"src/{project_name}/utils/__init__.py",  # Initialization file for utils subdirectory
    f"src/{project_name}/config/__init__.py",  # Initialization file for config subdirectory
    f"src/{project_name}/config/configuration.py",  # Configuration file for project
    f"src/{project_name}/pipeline/__init__.py",  # Initialization file for pipeline subdirectory
    f"src/{project_name}/entity/__init__.py",  # Initialization file for entity subdirectory
    f"src/{project_name}/constants/__init__.py",  # Initialization file for constants subdirectory
    "config/config.yaml",  # YAML configuration file (outside src)
    "dvc.yaml",  # DVC configuration file (outside src)
    "params.yaml",  # Parameter configuration file (outside src)
    "requirements.txt",  # Text file listing project dependencies
    "setup.py",  # Python setup script for packaging
    "research/trials.ipynb",  # Jupyter Notebook for research experiments
    "templates/index.html",  # HTML template file
]

# Loop through each file/directory in the list
for filepath in list_of_files:

    # Convert the filepath to a Path object (more robust)
    filepath = Path(filepath)

    # Extract directory path and filename
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist (using os.makedirs for efficiency)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if file exists and is empty (or doesn't exist)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # No content needed for empty files
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
