import requests
from fastapi.encoders import jsonable_encoder

import src.app as app
from src.app.view.view_clinicaltrials import response_studies

router = app.router


@router.get("/api/v2/studies")
async def get_studies():
    # T - 1:
    # In below only took one pages, nextPageToken should be used.
    pooled_studies = app.get_clinicaltrials

    return pooled_studies


@router.post("/post_studies")
async def post_studies():
    mapped_studies = app.post_clinicaltrials()

    return jsonable_encoder(response_studies(mapped_studies))
