import os
from pathlib import Path

project_name = "scorePrediction"
list_of_files = [
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/__init__.py",    
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/utils/__init_.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "Docker.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
         print(f"file is already present at: {filepath}")

