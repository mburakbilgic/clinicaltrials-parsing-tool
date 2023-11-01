from typing import Dict, List

from src.model.request_clinicaltrials import RequestStudiesClinicalTrial
from src.model.response_clinicaltrials import ResponseClinicalTrial


def request_studies(data: RequestStudiesClinicalTrial) -> List:
    return [data]


def response_studies(data: ResponseClinicalTrial) -> Dict:
    return {"clinicaltrial_data": data}
