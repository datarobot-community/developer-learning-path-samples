#!/bin/bash

# 01 - Importing data into DataRobot - From a local file
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/importing-data-into-datarobot/ta-p/2779

ENDPOINT=$YOUR_DR_URL/api/v2/projects/

curl -v \
-X POST \
-H "Authorization: Bearer $API_KEY" \
-H "Content-Type: multipart/form-data" \
-F file=@$FILE_PATH \
$ENDPOINT
