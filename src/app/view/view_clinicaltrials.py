from typing import Dict

from src.app.model.response_clinicaltrials import ResponseClinicalTrial


def clinicaltrials_response(data: ResponseClinicalTrial) -> Dict:
    return {"clinicaltrial_data": data}
