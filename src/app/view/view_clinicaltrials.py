from typing import Dict

from src.app.model.response_clinicaltrials import ResponseClinicalTrial


def response_studies(data: ResponseClinicalTrial) -> Dict:
    return {"clinicaltrial_data": data}
