import os
from pathlib import Path #finds os itself - appends path accordingly (win - \ , unix or linux -  /(back slash)
import logging #log-track details, will help in debugging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s : %(levelname)s]: %(message)s'
)

while True:
    project_name = input('Give Project Name: ')
    
    if project_name != "":
        break 

logging.info(f"Creating project :->  {project_name}")

# REF - How to make python packages : https://packaging.python.org/en/latest/tutorials/packaging-projects/
#list of files:
list_of_files = [".github/workflow/.gitkeep", #dummy file for now just to push to github
                 f"src/{project_name}/__init__.py", #making it package
                 f"tests/__init__.py", #for testing purposes - to create a robust application
                 f"tests/unit/__init__.py", #for all unit test
                 f"tests/integration/__init__.py", #for all integration test
                 "init_setup.sh", #for basics conda env setup
                 "requirements.txt", #main requirements
                 "requirements_dev.txt", #used only for testing
                 "setup.py", #for doing basic setup | more requirements 
                 "pyproject.toml", 
                 "setup.cfg",
                 "tox.ini" #to test package with different versions of python 
                 ]

# lets create all above files 
for filepath in list_of_files:
    filepath = Path(filepath) #take care of file paths of different os
    filedir, filename = os.path.split(filepath) #--> ("",xy.py), for directory give ""
    #if file directory is empty i.e. we have a file only ^, then create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #exist_ok true so it will not through error if dir already exists
        logging.info(f"Created directory at: {filedir} for file: {filename}") #logging process information
    #if code will rerun all files data will be erased | for that 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #if path does not exist or size of file == 0
        with open(filepath, "w") as f: #create an empty file using write operation
            pass
        logging.info(f"Created new file: {filename} at path: {filepath}")   
    else: 
        logging.info(f"Already have file at path: {filepath}")