import src
import requests


class Worker:

    def __init__(self):
        self.response = requests.get(src.api_url, params=src.params)

    def func_thread_settings(self):
        # T - 3
        # thread options required about chunksize process
        pass

    def func_get_clinicaltrials(self):
        if self.response.status_code == 200:
            data = self.response.json()
            studies = data["studies"]
            return studies
        else:
            return {"error": "Request failed"}

    def func_post_clinicaltrials(self):
        # T - 2
        # index for each trials
        studies = self.func_get_clinicaltrials()

        clinical_trials = []

        for each in range(len(studies)):
            print(each)
            """clinical_trials.append({
                "nct_id": studies[each]["protocolSection"]["identificationModule"]["nctId"],
                "brief_title": studies[each]["protocolSection"]["identificationModule"]["briefTitle"],
                "official_title": studies[each]["protocolSection"]["identificationModule"]["officialTitle"],
                "status_verified_date": studies[each]["protocolSection"]["statusModule"]["statusVerifiedDate"],
                "overall_status": studies[each]["protocolSection"]["statusModule"]["overallStatus"],
                "brief_summary": studies[each]["protocolSection"]["descriptionModule"]["briefSummary"],
                "detailed_description": studies[each]["protocolSection"]["descriptionModule"]["detailedDescription"],
                "conditions": studies[each]["protocolSection"]["conditionsModule"]["conditions"],
                "study_type": studies[each]["protocolSection"]["designModule"]["studyType"],
                "phases": studies[each]["protocolSection"]["designModule"]["phases"],
                "allocation": studies[each]["protocolSection"]["designModule"]["designInfo"]["allocation"],
                "intervention_model": studies[each]["protocolSection"]["designModule"]["designInfo"][
                    "interventionModel"],
                "primary_purpose": studies[each]["protocolSection"]["designModule"]["designInfo"]["primaryPurpose"],
                "masking": studies[each]["protocolSection"]["designModule"]["designInfo"]["maskingInfo"]["masking"],
                "count": studies[each]["protocolSection"]["designModule"]["enrollmentInfo"]["count"],
                "type": studies[each]["protocolSection"]["designModule"]["enrollmentInfo"]["type"],
                "eligibility_criteria": studies[each]["protocolSection"]["eligibilityModule"]["eligibilityCriteria"],
                "healthy_volunteers": studies[each]["protocolSection"]["eligibilityModule"]["healthyVolunteers"],
                "sex": studies[each]["protocolSection"]["eligibilityModule"]["sex"],
                "minimum_age": studies[each]["protocolSection"]["eligibilityModule"]["minimumAge"],
                "std_ages": studies[each]["protocolSection"]["eligibilityModule"]["stdAges"]
            })"""

        print(clinical_trials)

    def func_log(self):
        # T - 4
        # log options
        pass
