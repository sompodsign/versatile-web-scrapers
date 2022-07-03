from bs4 import BeautifulSoup
import requests
import re


class Scrape:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def get_title(self):
        return self.soup.title.string

    def get_html(self):
        return self.soup.prettify()


class DigitalOcean(Scrape):
    def __init__(self, url):
        super().__init__(url)

    def get_all_tutorial_links(self):
        return self.soup.find_all('a', href=re.compile('/community/tutorials/.*'))




digitalOcean = DigitalOcean('https://www.digitalocean.com/community/tutorials')

print(digitalOcean.get_all_tutorial_links())
