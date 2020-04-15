#!/bin/bash

# 03 - Get the prediction server ID
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/get-the-prediction-server-id/ta-p/2778

ENDPOINT=$YOUR_DR_URL/api/v2/predictionServers/

curl -v \
-H "Authorization: Bearer $API_KEY" \
$ENDPOINT