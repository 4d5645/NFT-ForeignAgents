from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import wikipediaapi
import numpy as np
import translators as ts

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B8%D0%BD%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D0%BE%D0%B2_(%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F)'
forgein_agents = {'nonprofit_org':0, 'mass_media':1, 'individual_media':2, 'individuals':3, 'unregistered_public_associations':4}

def create_driver(link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    drivet_url = driver.get(link)
    return driver

def parse_wiki(driver, forgein_agents):
    for nameofgroup, numberofgroup in zip(forgein_agents.keys(), forgein_agents.values()):
        chronobiology_content = driver.page_source
        chronobiology_soup = BeautifulSoup(chronobiology_content)
        tables = chronobiology_soup.findAll('table', attrs={'class':'wide sortable jquery-tablesorter'})
        df = pd.read_html(str(tables[numberofgroup]))
        df = pd.DataFrame(df[0])
        if nameofgroup == 'nonprofit_org' or nameofgroup == 'mass_media' or nameofgroup == 'unregistered_public_associations':
            df.to_csv(f"{nameofgroup}.csv")
        else:
            person = dict()
            table = tables[numberofgroup].findAll('tr')
            for row in table:
                columns = row.findAll('td')
                for i, col in enumerate(columns):
                    if i == 1:
                        if col.find('a'):
                            name = col.find('a').text.rstrip()
                            link_name = col.find('a').get('title')
                            link = col.find('a').get('href')
                            person[str(name)] = ['https://ru.wikipedia.org' + str(link), link_name]

            name_link = pd.DataFrame(person)
            name_link = name_link.T.reset_index()
            name_link = name_link.rename(columns={'index': 'Имя', 0: 'link', 1: 'wiki_name'})
            result = df.merge(name_link, how='left', on='Имя')
            result = result.fillna(-6022002)
            wiki_wiki = wikipediaapi.Wikipedia('ru')
            result["wiki_summary_ru"] = np.nan
            result["wiki_summary_eng"] = np.nan
            for i, name in enumerate(result['wiki_name']):
                page_py = wiki_wiki.page(name)
                summary = page_py.summary
                translated = ts.google(summary)
                if name != "NaN":
                    result["wiki_summary_ru"][i] = summary
                    result['wiki_summary_eng'][i] = translated
                else:
                    result["wiki_summary_ru"][i] = str("NaN") 
                    result['wiki_summary_eng'][i] = str("NaN") 
            result.to_csv(f"{nameofgroup}.csv")

if __name__ == "__main__":
    driver_Chrome = create_driver(url)
    parse_wiki(driver_Chrome, forgein_agents)