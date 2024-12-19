from jobs.abt_import import AbtImport

class JobManager:
    def __init__(self, browser):
        self.browser = browser

    def run_jobs(self, job_name):
        match job_name:
            case "abt_import":
                job = AbtImport(self.browser)
                job.run_job()