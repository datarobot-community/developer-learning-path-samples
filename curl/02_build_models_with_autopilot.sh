#!/bin/bash

# 02 - Build models using DataRobot Autopilot
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/deploy-a-model/ta-p/2780

# Replace YOUR_PROJECT_ID with your actual project ID - the output of importing data, or in your DataRobot GUI
ENDPOINT=$YOUR_DR_URL/api/v2/projects/YOUR_PROJECT_ID/aim/

# Target is the name of the column that you are trying to predict. Change if using a different dataset than default.
TARGET="readmitted"

curl -v \
-X PATCH \
-H "Authorization: Token $API_KEY" \
-H "Content-Type: application/json" \
-d "{\"target\":\"$TARGET\", \"mode\":\"auto\", \"quickrun\":true}" \
$ENDPOINT