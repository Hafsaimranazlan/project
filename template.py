import os
import logging 
from pathlib import Path

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -- %(message)s')


project_name='ml_project'


list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_intity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for file_path in list_of_files:
    filepath=Path(file_path)
    filedir,filename=os.path.split(filepath)
    

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directries : {filedir} for the : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating emptly file:{filepath}")

    else:
        logging.info(f"{filename} already exist")
        