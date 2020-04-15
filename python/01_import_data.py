# 01 - Import Data from a local file
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/importing-data-into-datarobot/ta-p/2779

# Environment setup

import os
import datarobot as dr

API_KEY = os.environ["API_KEY"]
YOUR_DR_URL = os.environ["YOUR_DR_URL"]
FILE_PATH = os.environ["FILE_PATH"]
ENDPOINT = YOUR_DR_URL+"/api/v2"

# Instantiate DataRobot instance
dr.Client(
    token=API_KEY, 
    endpoint=ENDPOINT
)

# Create project from a file
project = dr.Project.create(FILE_PATH, project_name='Diabetes')

print('Project with name %(name)s created. \n Project id is %(id)s.' % {"name": project.project_name, "id": project.id })


