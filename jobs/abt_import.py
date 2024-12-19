from jobs.jobs import Jobs
from selenium.webdriver.common.by import By
from datetime import datetime
from config import kmc_username, kmc_password
import os

class AbtImport(Jobs):
    def __init__(self, browser):
        super().__init__(browser)
        month = datetime.now().strftime("%m")
        year = datetime.now().strftime("%Y")
        # Local Host
        kmc_url_start = 'http://localhost:8080/#/'
        # Live
        # kmc_url_start = 'https://residentmap.kmcmh.com/#/'

        self.properties_info = [
            {
                'name': "Arapaho Village", 
                'abt_url': 'http://12.175.8.66/Usage%20Reports/All/KMC%20Arapaho%20Village.html', 
                'kmc_url': f'{kmc_url_start}properties/76/imports', 
                'import_date': f"{month}/15/{year}",
                'file_path': os.path.join(self.browser.download_dir, f"SPUD for KMC Arapaho Village {month}_15_{year}.csv")
            },
            {
                'name': "Haven Cove",
                'abt_url': 'http://12.175.8.66/Usage%20Reports/All/KMC%20Haven%20Cove.html',
                'kmc_url': f'{kmc_url_start}properties/66/imports',
                'import_date': f"{month}/10/{year}",
                'file_path': os.path.join(self.browser.download_dir, f"SPUD for KMC Haven Cove {month}_10_{year}.csv")
            },
            {
                'name': "Lake Villa",
                'abt_url': 'http://12.175.8.66/Usage%20Reports/All/KMC%20Lake%20Villa.html',
                'kmc_url': f'{kmc_url_start}properties/59/imports',
                'import_date': f"{month}/10/{year}",
                'file_path': os.path.join(self.browser.download_dir, f"SPUD for KMC Lake Villa {month}_10_{year}.csv")
            },
        ]

    def run_job(self):
        for property in self.properties_info:

            if not os.path.exists(property['file_path']):
                self.download_from_abt(property)

            self.upload_to_manage_portal(property)

    def download_from_abt(self, property):
        self.browser.driver.get(property['abt_url'])
        self.browser.find_click(By.XPATH, '//input[@type="submit" and @value="Export a Readings File"]')
        self.browser.send_keys(By.XPATH, '//input[@type="TEXT" and @name="The Date"]', property['import_date'])
        self.browser.find_select(By.NAME, 'ExportFormat', 'Starnik')
        self.browser.find_click(By.XPATH, '//input[@type="submit" and @value="Go!"]')
        self.browser.wait_for_downloads()

    def upload_to_manage_portal(self, property):
        self.browser.driver.get(property['kmc_url'])
        self.browser.wait_login(kmc_username, kmc_password)
        self.select_kmc_element(property)


    def select_kmc_element(self, property):
        dropdowns = [
            {'value': '//div[@class="flex-row card-text"]//details[@class="auto_complete"]', 'key': '//li[normalize-space(text())="Utility Reads - ABT"]'},
            {'value': '//div[@class="alert-info full-width"]//details[@class="auto_complete"]', 'key': '//li[normalize-space(text())="Water"]'}
            ]
        for dropdown in dropdowns:
            self.browser.wait_click(By.XPATH, dropdown['value'])
            self.browser.wait_for_presence_of_element(By.CSS_SELECTOR, 'ul.popup')
            self.browser.wait_click(By.XPATH, dropdown['key'])

        self.browser.wait_for_presence_of_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(property['file_path'])
        self.browser.wait_click(By.XPATH, '//button[@type="button" and contains(@class, "primary push_button")]')
        self.browser.wait_for_page_load()



