from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

website = 'https://www.adamchoi.co.uk/overs/detailed'
driver = webdriver.Chrome(options=options)
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Spain")

time.sleep(2)
matches = driver.find_elements(By.TAG_NAME, 'tr')
date = []
home = []
score = []
away = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away.append(match.find_element(By.XPATH, './td[4]').text)



df = pd.DataFrame({'date': date, 'home': home, 'score': score, 'away': away})
df.to_csv('spain.csv')