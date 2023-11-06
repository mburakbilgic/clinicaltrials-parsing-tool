import src
from collections import defaultdict

import requests

from src.model.response_clinicaltrials import ResponseClinicalTrial as ResBody


class Worker:

    def __init__(self):
        self.response = requests.get(src.api_url, params=src.params)

    def func_thread_settings(self):
        # T - 3
        # thread options required about chunksize process
        pass

    def func_fillna_studies(self, sections):
        keys_to_check = [
            ("identificationModule", "nctId"),
            ("identificationModule", "briefTitle"),
            ("identificationModule", "officialTitle"),
            ("statusModule", "statusVerifiedDate"),
            ("statusModule", "overallStatus"),
            ("descriptionModule", "briefSummary"),
            ("descriptionModule", "detailedDescription"),
            ("conditionsModule", "conditions"),
            ("designModule", "studyType"),
            ("eligibilityModule", "eligibilityCriteria")
        ]

        for key, subkey in keys_to_check:
            if key in sections and subkey in sections[key]:
                continue
            else:
                sections[key] = sections.get(key, {})
                sections[key][subkey] = "N_A"

        return sections

    def func_get_clinicaltrials(self):
        if self.response.status_code == 200:
            data = self.response.json()
            studies = data["studies"]
            return studies
        else:
            return {"error": "Request failed"}

    def func_post_clinicaltrials(self):
        studies = self.func_get_clinicaltrials()

        clinical_trials = []

        for each in range(len(studies)):
            section = studies[each]["protocolSection"]

            self.func_fillna_studies(section)

            identificationModule = section["identificationModule"]
            statusModule = section["statusModule"]
            descriptionModule = section["descriptionModule"]
            conditionsModule = section["conditionsModule"]
            designModule = section["designModule"]
            eligibilityModule = section["eligibilityModule"]

            response = ResBody(
                nct_id=identificationModule["nctId"],
                brief_title=identificationModule["briefTitle"],
                official_title=identificationModule["officialTitle"],
                status_verified_date=statusModule["statusVerifiedDate"],
                overall_status=statusModule["overallStatus"],
                brief_summary=descriptionModule["briefSummary"],
                detailed_description=descriptionModule["detailedDescription"],
                conditions=conditionsModule["conditions"],
                study_type=designModule["studyType"],
                eligibility_criteria=eligibilityModule["eligibilityCriteria"]
            )

            clinical_trials.append({
                "nct_id": response.nct_id,
                "brief_title": response.brief_title,
                "official_title": response.official_title,
                "status_verified_date": response.status_verified_date,
                "overall_status": response.overall_status,
                "brief_summary": response.brief_summary,
                "detailed_description": response.detailed_description,
                "conditions": response.conditions,
                "study_type": response.study_type,
                "eligibility_criteria": response.eligibility_criteria
            })

        return clinical_trials

    def func_log(self):
        # T - 4
        # log options
        pass
