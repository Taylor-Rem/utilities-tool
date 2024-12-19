import sys
from front_end.app import App
from tools.browser import Browser
from jobs.job_manager import JobManager
from PyQt5.QtWidgets import QApplication

# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)

    browser = Browser()
    job_manager = JobManager(browser)
    window = App(job_manager)

    window.show()
    
    sys.exit(app.exec_())
