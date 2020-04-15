# 04 - Deploy a model
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/deploy-a-model/ta-p/2780

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

#TODO: Replace with your values
MODEL_ID = "YOUR_MODEL_ID" # Get from step 03
PREDICTION_SERVER_ID = "YOUR_PREDICTION_SERVER_ID" #Get from step 04

deployment = dr.Deployment.create_from_learning_model(
      model_id = MODEL_ID, 
      label='New Deployment', 
      description='A new deployment',
      default_prediction_server_id=PREDICTION_SERVER_ID)

print("Deployment created.")
print(deployment)
