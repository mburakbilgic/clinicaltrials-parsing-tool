from fastapi.encoders import jsonable_encoder

import src
from src.worker.worker_main import Worker
from src.view.view_clinicaltrials import request_studies, response_studies


router = src.router


@router.get("/api/v2/studies")
async def get_studies():
    # T - 1:
    # In below only took one pages, nextPageToken should be used.
    pooled_studies = Worker().func_get_clinicaltrials()

    return request_studies(pooled_studies)


@router.post("/post_studies")
async def post_studies():
    mapped_studies = Worker().func_post_gcs()

    return response_studies(mapped_studies)
