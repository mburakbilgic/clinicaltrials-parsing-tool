from fastapi.encoders import jsonable_encoder

import src
from src.view.view_clinicaltrials import response_studies

router = src.router


@router.get("/api/v2/studies")
async def get_studies():
    # T - 1:
    # In below only took one pages, nextPageToken should be used.
    pooled_studies = src.get_clinicaltrials

    return pooled_studies


@router.post("/post_studies")
async def post_studies():
    mapped_studies = src.post_clinicaltrials()

    return jsonable_encoder(response_studies(mapped_studies))
