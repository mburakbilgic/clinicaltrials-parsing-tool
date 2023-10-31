from fastapi import FastAPI

from src.controller import controller_clinicaltrials

application = FastAPI()

application.include_router(controller_clinicaltrials.router)

"""
in controller section; below app.get should be like this;
import requests

@router.get("/api/v2/studies")
async def [function_name]
    ...
    ...
    return data

### this below should be change to above
@app.get("/api/v2/studies")
def get_studies():
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        studies = data["studies"]
        return studies
    else:
        return {"error": "İstek başarısız"}"""

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(application, host="0.0.0.0", port=8000)
