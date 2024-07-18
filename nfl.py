from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

website = 'https://www.pro-football-reference.com/years/2024/games.htm'
driver = webdriver.Chrome(options=options)
driver.get(website)

games = driver.find_element(By.ID, 'games')
print(games.text)