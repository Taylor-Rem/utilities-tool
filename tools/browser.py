from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(), options=Options())

    def close(self):
        if self.driver:
            self.driver.quit()
            self.driver = None