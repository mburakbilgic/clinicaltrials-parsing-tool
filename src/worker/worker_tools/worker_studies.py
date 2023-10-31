import requests

import src


class Studies:

    def __init__(self):
        self.response = requests.get(src.api_url, params=src.params)
        self.studies = None

    def get_clinicaltrials(self):
        if self.response.status_code == 200:
            data = self.response.json()
            self.studies = data["studies"]
            return self.studies
        else:
            return {"error": "Request failed"}

    def post_clinicaltrials(self):
        # T - 3
        # studies mapping
        pass
