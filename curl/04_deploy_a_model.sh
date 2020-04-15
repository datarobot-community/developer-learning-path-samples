#!/bin/bash

# 04 - Deploying a trained model
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/deploy-a-model/ta-p/2780

ENDPOINT=$YOUR_DR_URL/api/v2/deployments/fromLearningModel/

# Replace YOUR_MODEL_ID with the actual model ID. You can find this in the URL of the model (second number)
MODEL_ID=YOUR_MODEL_ID

# Replace YOUR_PREDICTION_SERVER_ID with actual prediction server Id - the output of the previous step.
PREDICTION_SERVER_ID=YOUR_PREDICTION_SERVER_ID

curl -v \
-X POST \
-H "Authorization: Bearer $API_KEY" \
-H "Content-Type: application/json" \
--data "{\"modelId\": \"$MODEL_ID\", \"defaultPredictionServerId\": \"$PREDICTION_SERVER_ID\", \"description\": \"A description\", \"label\": \"A label\"}" \
$ENDPOINT