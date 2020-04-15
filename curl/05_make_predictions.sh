#!/bin/bash

# 05 - Make a prediction
# Corresponding article: https://community.datarobot.com/t5/guided-ai-learning/make-predictions/ta-p/2782

# Replace YOUR_MODEL_ID with the output from 04_deploy_a_model.sh
DEPLOYMENT_ID=YOUR_MODEL_ID

#Replace YOUR_PREDICTION_SERVER with the output of 03_get_prediction_server.sh
PRED_ENDPOINT="YOUR_PREDICTION_SERVER/predApi/v1.0/deployments/$DEPLOYMENT_ID/predictions"

#Replace YOUR_DATAROBOT_KEY with the output of 03_get_prediction_server.sh
DATAROBOT_KEY=YOUR_DATAROBOT_KEY

curl -v \
-X POST \
-H "Authorization: Bearer $API_KEY" \
-H "datarobot-key: $DATAROBOT_KEY" \
-H "Content-Type: application/json" \
--data-raw '[
  {
    "ID": 1,
    "race": "Caucasian",
    "gender": "Female",
    "age": "[50-60)",
    "weight": "?",
    "admission_type_id": "Elective",
    "discharge_disposition_id": "Discharged to home",
    "admission_source_id": "Physician Referral",
    "time_in_hospital": 1,
    "payer_code": "CP",
    "medical_specialty": "Surgery-Neuro",
    "num_lab_procedures": 35,
    "num_procedures": 4,
    "num_medications": 21,
    "number_outpatient": 0,
    "number_emergency": 0,
    "number_inpatient": 0,
    "diag_1": 723,
    "diag_2": 723,
    "diag_3": 719,
    "number_diagnoses": 9,
    "max_glu_serum": "None",
    "A1Cresult": "None",
    "metformin": "No",
    "repaglinide": "No",
    "nateglinide": "No",
    "chlorpropamide": "No",
    "glimepiride": "No",
    "acetohexamide": "No",
    "glipizide": "No",
    "glyburide": "No",
    "tolbutamide": "No",
    "pioglitazone": "No",
    "rosiglitazone": "No",
    "acarbose": "No",
    "miglitol": "No",
    "troglitazone": "No",
    "tolazamide": "No",
    "examide": "No",
    "citoglipton": "No",
    "insulin": "No",
    "glyburide.metformin": "No",
    "glipizide.metformin": "No",
    "glimepiride.pioglitazone": "No",
    "metformin.rosiglitazone": "No",
    "metformin.pioglitazone": "No",
    "change": "No",
    "diabetesMed": "No",
    "diag_1_desc": "Spinal stenosis in cervical region",
    "diag_2_desc": "Spinal stenosis in cervical region",
    "diag_3_desc": "Effusion of joint, site unspecified"
  }]' \
$PRED_ENDPOINT 


