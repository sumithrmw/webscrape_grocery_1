import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np


driver = webdriver.Chrome("C:\\Users\\sumit\\Desktop\\Misc\\chromedriver.exe")

def superstore(items):
    driver.get("https://www.realcanadiansuperstore.ca/")
    driver.implicitly_wait(3)
    element = driver.find_element(By.CLASS_NAME, "search-input__input")
    element.send_keys(items)
    element.send_keys(Keys.ENTER)
    driver.implicitly_wait(3)



eow = superstore('eggs')


akr = driver.find_elements(By.XPATH, '//span[@ class="product-name__item product-name__item--brand"]')
sdr = driver.find_elements(By.XPATH, '//span[@ class="product-name__item product-name__item--name"]')
price = driver.find_elements(By.XPATH, '//span[@ class="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value"]')

for i in akr:
    brand = [i.text]
    print(brand)
for i in sdr:
    name = [i.text]
    print(name)
for i in price:
    p =[i.text]
    print(p)


    with open('price', 'a', encoding='UTF -8', newline='' ) as ef:
           for k in brand:
              ef.write(str(brand) + " " + str(name)+" " + str(p) +"\n")


driver.close()













