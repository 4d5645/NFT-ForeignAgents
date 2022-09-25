from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time
import pandas as pd


username = " "
password = " "

def create_driver(main_link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    drivet_url = driver.get(main_link)
    return driver

all_full_links = []
def parse_caption(driver):
        chronobiology_content = driver.page_source
        chronobiology_soup = BeautifulSoup(chronobiology_content)
        button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
        button.click()
        username_input = driver.find_element_by(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input').send_keys(username)
        driver.find_element(By.XPATH, "input[name='password']").send_keys(password)
        driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button").click()
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
        button.click()
        text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span')
        print(text.text)

url = 'https://www.instagram.com/'
driver_Chrome = create_driver(url)
parse_caption(driver_Chrome)


# /html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]

# /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span
# /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span
# /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span