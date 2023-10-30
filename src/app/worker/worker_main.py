from worker_tools.worker_studies import Studies

class Worker:

    def __init__(self):
        pass

    def func_thread_settings(self):
        # T - 2
        # thread options required about chunksize process
        pass

    def func_get_clinicaltrials(self):
        return_object = Studies.get_clinicaltrials

        return return_object

    def func_post_clinicaltrials(self):
        return_object = Studies.post_clinicaltrials

        return return_object

    def func_log(self):
        # T - 4
        # log options
        pass
