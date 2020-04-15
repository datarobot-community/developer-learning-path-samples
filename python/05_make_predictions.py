# 05 - Make predictions on a model
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/make-predictions/ta-p/2782

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

PROJECT_ID = "YOUR_PROJECT_ID" # Get from 01 - import data or look it up using dr.Projects.list() 
MODEL_ID = "YOUR_MODEL_ID" # Get from project.get_models()

project = dr.Project.get(PROJECT_ID) 
model = dr.Model.get(project=PROJECT_ID, model_id=MODEL_ID)
					
# First upload the dataset you'd like ot make predictions on
dataset_from_path = project.upload_dataset('../common/diabetes_predictions.csv')

print("Starting prediction job")
predict_job = model.request_predictions(dataset_from_path.id) 

print(predict_job)

# Wait for predictions to complete
predictions = predict_job.get_result_when_complete()

print("Finished making predictions")
print(predictions)
