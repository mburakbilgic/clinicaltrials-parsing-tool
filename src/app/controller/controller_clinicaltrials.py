from fastapi.encoders import jsonable_encoder

import src.app as app
from src.app.view.view_clinicaltrials import clinicaltrials_response

router = app.router


@router.post("/raw_studies")
async def clinicaltrials():
    raw_clinicaltrials = app.raw_clinicaltrials

    return jsonable_encoder(clinicaltrials_response(raw_clinicaltrials))
