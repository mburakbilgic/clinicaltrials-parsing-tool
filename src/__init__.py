import os

import yaml
import requests
from fastapi import APIRouter, FastAPI
from fastapi.openapi.models import OpenAPI

MAIN_PATH = os.getcwd()
CONFIG_PATH = os.path.join(MAIN_PATH, "system_docs\\config\\ctg-oas-v2.yaml")
GCS_CONFIG_PATH = os.path.join(MAIN_PATH, "system_docs\\config\\monolith-technology-83cdc098a399.json")
DATA_FILES = os.path.join(MAIN_PATH, "system_docs\\data")
LOG_FILES = os.path.join(MAIN_PATH, "system_docs\\logs")

router = APIRouter()

# OpenAPI, Request URL and Query Parameters settings
with open(CONFIG_PATH, "r") as file:
    openapi_config = yaml.safe_load(file)

# Google SDK Credential Configuration
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(GCS_CONFIG_PATH)

local_app = FastAPI()
local_app.openapi = OpenAPI(**openapi_config)

servers = openapi_config.get("servers", [])
if servers:
    server_url = servers[0].get("url")
else:
    server_url = ""

api_url = f"{server_url}/studies"
params = {
    "pageSize": 1000,  # Results of each page
    "pageToken": None,  # In first page this should be empty
    "query.cond": "cancer",
    "filter.overallStatus": "RECRUITING"
}
response = requests.get(api_url, params=params)
