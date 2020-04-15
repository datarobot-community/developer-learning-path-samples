# 03 - Get Prediction server Id
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/get-the-prediction-server-id/ta-p/2778

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

prediction_server_id = dr.PredictionServer.list()[0].id
print(prediction_server_id)

