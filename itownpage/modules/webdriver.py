import os, sys, time, datetime
# import chromedriver_binary # docker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Mac or Docker
is_local = True
if is_local:
    DRIVER_PATH = '/usr/local/bin/chromedriver'
    CHROME_BIN_PATH = None
else:
    DRIVER_PATH = 'chromedriver'
    CHROME_BIN_PATH = '/usr/bin/google-chrome'


class Chrome(object):

    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--lang=ja')
        # only docker
        if CHROME_BIN_PATH:
            options.binary_location = CHROME_BIN_PATH
        driver = webdriver.Chrome(DRIVER_PATH, options=options)
        return driver

    def get_screen_shot(self) -> None:
        dt = datetime.datetime.today()
        now = dt.strftime('%Y%m%d%H%M%S')
        self.driver.save_screenshot(f'./{now}.png')
        return None