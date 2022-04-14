import csv
import os

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome("C:\\Users\\sumit\\Desktop\\Misc\\chromedriver.exe")

def nofrills(items):
    driver.get("https://www.nofrills.ca/")
    driver.implicitly_wait(3)
    element = driver.find_element(By.CLASS_NAME, "search-input__input")
    element.send_keys(items)
    element.send_keys(Keys.ENTER)
    driver.implicitly_wait(3)

eow = nofrills('chicken')
brandname = []
itemname = []
price1 = []

akr = driver.find_elements(By.XPATH, '//span[@ class="product-name__item product-name__item--brand"]')
sdr = driver.find_elements(By.XPATH, '//span[@ class="product-name__item product-name__item--name"]')
price = driver.find_elements(By.XPATH, '//span[@ class="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value"]')

for k in akr:
    akr = k.text
    brandname.append(akr)

for k in sdr:
    sdr = k.text
    itemname.append(sdr)

for k in price:
    price = k.text
    price1.append(price)

# df = pd.DataFrame(brandname[:25], brandname[:25], price1[:25])
value = np.array([brandname[0:20], itemname[0:20], price1[0:20]])
print(value)

df = pd.DataFrame(value).T
print(df)

# df = pd.DataFrame({'Column1': value[0], 'Column2': value[1], 'Coloumn3': value[3]})
df.to_csv('nofrillsdata.csv', encoding='utf-8')

driver.close()
