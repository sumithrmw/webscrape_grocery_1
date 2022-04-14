import csv
import os
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\sumit\\Desktop\\Misc\\chromedriver.exe")


class storegrab:
     def __init__(self, name, link, filename):
         self.name = name
         self.link = link
         self.filename= filename
         driver.get(link)
         driver.implicitly_wait(3)
         element = driver.find_element(By.CLASS_NAME, "search-input__input")
         element.send_keys(self.name)
         element.send_keys(Keys.ENTER)
         driver.implicitly_wait(3)

         brandname = []
         itemname = []
         price1 = []

         akr = driver.find_elements(By.XPATH, '//span[@ class="product-name__item product-name__item--brand"]')
         sdr = driver.find_elements(By.XPATH, '//span[@ class="product-name__item product-name__item--name"]')
         price = driver.find_elements(By.XPATH,
                                      '//span[@ class="price__value selling-price-list__item__price selling-price-list__item__price--now-price__value"]')

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

         ask = filename.strip()

         df.to_csv(f'{ask}''.csv' ,index=False, header= 0, encoding='utf-8')

with open('groclist.txt', encoding='utf-8') as ef:
    for i in ef:
        print(i)
        adv = storegrab(i, "https://www.nofrills.ca/", f'{i}')



