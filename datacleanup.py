import csv
import numpy as np
import os
import pandas as pd
from os import listdir
import glob

fol = ("C:\\Users\\sumit\\Desktop\\data\\grocerystore\\supersstore")

n = 0
for file in glob.glob("C:\\Users\\sumit\\Desktop\\data\\grocerystore\\supersstore\\*.csv",):
    n = n+1
    #print(file)
    #print(n)

data1 = pd.read_csv("C:\\Users\\sumit\\Desktop\\data\\grocerystore\\supersstore\\bananas berries.csv")
der = pd.DataFrame(data1).T
#asr = der.iloc[1:,]

seq = der[0].str.split(',',expand=True)
#index = list(zip(*asr))
#print(index)

shape = der.shape
print('\nDataFrame Shape :', shape)
print('\nNumber of rows :', shape[0])
print('\nNumber of columns :', shape[1])

seq.to_csv('aaaa.csv', index=False, header= 0 , encoding='utf-8')


print(der)