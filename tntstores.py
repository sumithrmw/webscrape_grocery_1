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
class tnt:
    def __init__(self, name, link, filename):
        self.name = name
        self.link = link
        self.filename = filename
        driver.get(link)
        driver.implicitly_wait(3)
        element = driver.find_element(By.XPATH , '//input[@ value=""]')
        element.send_keys(name)
        element.send_keys(Keys.ENTER)
        driver.implicitly_wait(3)

        brandname = []
        price1 = []

        akr = driver.find_elements(By.XPATH, '//*[@ class="item-name-16V"]')
        price = driver.find_elements(By.XPATH, '//*[@ class="item-price-2Lk"]')

        for k in akr:
           akr = k.text
           brandname.append(akr)

        for k in price:
           sdr = k.text
           price1.append(sdr)

        print(brandname)
        print(price1)

        value = np.array([brandname [0:20],price1[0:20]])
        df = pd.DataFrame(value).T

        ask = filename.strip()

        df.to_csv(f'{ask}.csv', index=False,header=0,  encoding='utf-8')

with open('groclist.txt', encoding='utf-8') as ef:
    for i in ef:
        print(i)
        adv = tnt(i, "https://www.tntsupermarket.com/", f'{i}')

driver.close()