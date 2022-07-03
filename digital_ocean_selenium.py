import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from driver_actions import DriverActions


class Scrape:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.driver_actions = DriverActions(self.driver)

    @staticmethod
    def parse_html(page_source):
        return BeautifulSoup(page_source, 'html.parser')

    def get_prettify(self, page_source):
        return self.parse_html(page_source).prettify()

    def get_title(self):
        return self.driver.title

    def get_html(self):
        self.soup = self.parse_html(self.driver.page_source)

    def close(self):
        self.driver.close()


class DigitalOcean(Scrape):
    def __init__(self, url):
        super().__init__(url)
        self.accept_cookies()

    def accept_cookies(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()

    def click_show_more_button(self):
        self.driver_actions = DriverActions(self.driver)
        button = self.driver.find_element(By.XPATH, '//*[contains(text(), "See more")]')
        self.driver_actions.click_on_web_element_using_javascript(button)
        time.sleep(4)

    def get_all_tutorial_links(self):
        return self.soup.find_all('a', href=re.compile('/community/tutorials/.*'))


digitalOcean = DigitalOcean('https://www.digitalocean.com/community/tutorials')


for i in range(5):
    digitalOcean.click_show_more_button()

digitalOcean.get_html()
print(len(digitalOcean.get_all_tutorial_links()))

digitalOcean.close()
