import os

import yaml
from fastapi import APIRouter, FastAPI
from fastapi.openapi.models import OpenAPI

from src.app.worker.worker_main import Worker

os.chdir(".")

MAIN_PATH = os.getcwd()
CONFIG_PATH = os.path.join(MAIN_PATH, "..\\config\\ctg-oas-v2.yaml")
DATA_FILES = os.path.join(MAIN_PATH, "..\\data")
LOG_FILES = os.path.join(MAIN_PATH, "..\\logs")

router = APIRouter()

set_thread = Worker().func_thread_settings()
get_clinicaltrials = Worker().func_get_clinicaltrials
post_clinicaltrials = Worker().func_post_clinicaltrials()
log_call = Worker().func_log

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
