import os

import yaml
import requests
from fastapi import APIRouter, FastAPI
from fastapi.openapi.models import OpenAPI

MAIN_PATH = os.getcwd()
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config", "ctg-oas-v2.yaml")
DATA_FILES = os.path.join(os.path.dirname(__file__), "data")
LOG_FILES = os.path.join(os.path.dirname(__file__), "logs")

router = APIRouter()

# OpenAPI, Request URL and Query Parameters settings
with open(CONFIG_PATH, "r") as file:
    openapi_config = yaml.safe_load(file)

local_app = FastAPI()
local_app.openapi = OpenAPI(**openapi_config)

servers = openapi_config.get("servers", [])
if servers:
    server_url = servers[0].get("url")
else:
    server_url = ""

api_url = f"{server_url}/studies"
params = {
    "pageSize": 10,  # Results of each page
    "pageToken": None,  # In first page this should be empty
    "query.cond": "cancer",
    "filter.overallStatus": "RECRUITING"
}
response = requests.get(api_url, params=params)
