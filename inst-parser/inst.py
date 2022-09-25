import sys
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

from private_data import username, password

username = username
password = password

def create_driver(main_link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    drivet_url = driver.get(main_link)
    return driver

posts = []
def parse_caption(driver):
    chronobiology_content = driver.page_source
    chronobiology_soup = BeautifulSoup(chronobiology_content)
    button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
    button.click()
    driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input').send_keys(username)
    driver.find_element(By.XPATH, "input[name='password']").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()
    j = 0
    while True or j != 10:
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
        button.click()
        text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span')
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
        button.click()
        posts.append(text.text)
    data = pd.DataFrame(posts)
    data.to_csv(sys.argv[2])

url = sys.argv[1]
driver_Chrome = create_driver(url)
parse_caption(driver_Chrome)
