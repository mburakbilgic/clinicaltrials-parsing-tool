import src
import requests


class Worker:

    def __init__(self):
        self.studies = None
        self.response = requests.get(src.api_url, params=src.params)

    def func_thread_settings(self):
        # T - 2
        # thread options required about chunksize process
        pass

    def func_get_clinicaltrials(self):
        if self.response.status_code == 200:
            data = self.response.json()
            self.studies = data["studies"]
            return self.studies
        else:
            return {"error": "Request failed"}

    def func_post_clinicaltrials(self):
        pass

    def func_log(self):
        # T - 4
        # log options
        pass
