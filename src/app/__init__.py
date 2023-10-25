import os

from fastapi import FastAPI
from fastapi.openapi.models import OpenAPI
import yaml

os.chdir(".")

MAIN_PATH = os.getcwd()
CONFIG_PATH = os.path.join(MAIN_PATH, "..\\config\\ctg-oas-v2.yaml")

with open(CONFIG_PATH, "r") as file:
    openapi_config = yaml.safe_load(file)

app = FastAPI()
app.openapi = OpenAPI(**openapi_config)

# OpenAPI belgesinden sunucu URL'sini alın
servers = openapi_config.get("servers", [])
if servers:
    server_url = servers[0].get("url")
else:
    server_url = ""

# API URL ve sorgu parametreleri
api_url = f"{server_url}/studies"
params = {
    "pageSize": 10,  # Sayfa başına sonuç sayısı
    "pageToken": None,  # İlk sayfada bu parametre boş olmalıdır
    "query.cond": "cancer",
    "filter.overallStatus": "RECRUITING"
}
