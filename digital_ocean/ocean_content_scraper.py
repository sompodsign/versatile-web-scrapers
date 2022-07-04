import re

import pandas as pd

from digital_ocean.digital_ocean_selenium import DigitalOcean


def get_content(link):
    tutorial_soup = DigitalOcean(link)
    tutorial_soup.get_html()
    title = tutorial_soup.soup.find('h1', class_=re.compile('HeadingStyles__StyledH1')).text
    content = tutorial_soup.soup.find('div', class_=re.compile('Markdown_markdown__'))
    return {'title': title, 'content': content}


def get_tutorial_links(csv):
    df = pd.read_csv(csv)
    return df['href'].to_list()


def get_tutorial_content():
    links = get_tutorial_links('digital_ocean_tutorials.csv')
    for link in links:
        content = get_content(link)
        print(content)


get_tutorial_content()
