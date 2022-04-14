import numpy as np
import os
import pandas as pd
from os import listdir
import glob

data1 = pd.read_csv("C:\\Users\\sumit\\PycharmProjects\\groceryportfolio\\aaaa.csv")

seq=pd.DataFrame(data1)

seq = data1[0].str.split(',',expand=True)
seq.to_csv('zzzz.csv', index=False , encoding='utf-8')


