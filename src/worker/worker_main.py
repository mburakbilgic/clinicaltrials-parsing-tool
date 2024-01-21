import src
import json
import tempfile

from google.cloud import storage

import requests
from fastapi import HTTPException

from src.model.response_clinicaltrials import ResponseClinicalTrial as ResBody


class Worker:

    def __init__(self):
        self.response = requests.get(src.api_url, params=src.params)
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket("monolith-technology_bucket-clinicaltrials")
        self.nextPageToken = None

    def func_get_clinicaltrials(self):
        all_studies = []
        while True:
            if self.response.status_code == 200:
                data = self.response.json()
                studies = data.get("studies", [])
                token = data.get("nextPageToken")
                all_studies.extend(studies)

                if token is not None:
                    src.params["pageToken"] = token
                    self.response = requests.get(src.api_url, params=src.params)
                    data = self.response.json()
                    studies = data["studies"]
                    all_studies.extend(studies)
                else:
                    break
            else:
                return {"error": "Request failed"}

        return all_studies

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

    def func_mapping_clinicaltrials(self):
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

        print(len(clinical_trials))

        return clinical_trials

    def func_post_gcs(self):
        try:
            file_name = "clinicaltrials.json"
            data = self.func_mapping_clinicaltrials()

            json_data = json.dumps(data, indent=2)

            ct_blob = self.bucket.blob(file_name)
            ct_blob.upload_from_string(data=json_data,
                                       content_type='application/json')

            return {"status": "success"}

        except HTTPException as e:
            raise e

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
