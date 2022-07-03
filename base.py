from selenium import webdriver
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
