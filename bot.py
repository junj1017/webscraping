from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

website = 'https://www.audible.com/search'
driver = webdriver.Chrome(options=options)
driver.get(website)

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')

products = container.find_elements(By.XPATH, './div/span/ul/li')

title = []
author = []
length = []

for product in products:
    title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
    author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
    length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

driver.quit()
df_books = pd.DataFrame({'title': title, 'author': author, 'length': length})

df_books.to_csv('books.csv', index=False)


