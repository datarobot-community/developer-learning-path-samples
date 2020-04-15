import os
import datarobot as dr 

# Environment setup
API_KEY = os.environ["API_KEY"]
YOUR_DR_URL = os.environ["YOUR_DR_URL"]
FILE_PATH = os.environ["FILE_PATH"]
ENDPOINT = YOUR_DR_URL+"/api/v2"

# Instantiate DataRobot instance
dr.Client(
    token=API_KEY, 
    endpoint=ENDPOINT
)

print("Creating project...")

project = dr.Project.create(FILE_PATH, project_name='Diabetes')

print('Project with name %(name)s created. \n Project id is %(id)s.' % {"name": project.project_name, "id": project.id })

print("Starting autopilot for training models...")
project.set_target(target='readmitted', mode=dr.AUTOPILOT_MODE.FULL_AUTO)

project.wait_for_autopilot()

print("Autopilot finished!")

all_models = project.get_models()
top_5_models = all_models[:5]
top_model = top_5_models[0]

print("Top performing model: ")
print(top_model)
print(top_model.id)
					
# First upload the dataset you'd like ot make predictions on
prediction_dataset = project.upload_dataset('../common/diabetes_predictions.csv')

print("Starting prediction job")
predict_job = top_model.request_predictions(prediction_dataset.id) 

print(predict_job)

# Wait for predictions to complete
predictions = predict_job.get_result_when_complete()

print("Finished making predictions")
print(predictions)



