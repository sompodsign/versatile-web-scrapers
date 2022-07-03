import re
import time

from selenium.webdriver.common.by import By

from base import BaseScraper


class DigitalOcean(BaseScraper):
    def __init__(self, url):
        super().__init__(url)
        self.accept_cookies()
        self.tutorial_links = []

    def accept_cookies(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()

    def click_show_more_button(self):
        button = self.driver.find_element(By.XPATH, '//*[contains(text(), "See more")]')
        self.driver_actions.click_on_web_element_using_javascript(button)
        time.sleep(4)

    def get_all_tutorial_links(self):
        return self.soup.find_all('a', href=re.compile('/community/tutorials/.*'))
