# 02 - Build models with Autopilot
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/build-models-with-autopilot/ta-p/2781

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

# Use dr.Project.list to look up previously created project
project = dr.Project.list(search_params={'project_name': 'Diabetes'})[0]

# Train models by calling project.set_target and Autopilot mode
print("Starting autopilot for training models...")
project.set_target(target='readmitted', mode=dr.AUTOPILOT_MODE.FULL_AUTO)

# Wait for Autopilot to finish
project.wait_for_autopilot()

print("Autopilot finished!")

# Get all trained models in a project. Models are ordered by their quality
all_models = project.get_models()
top_5_models = all_models[:5]
top_model = top_5_models[0]

print("Top performing model: ")
print(top_model)
print(top_model.id)
