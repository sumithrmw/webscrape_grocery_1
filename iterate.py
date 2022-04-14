import numpy as np
import os
import pandas as pd
from os import listdir
import glob
import random
import shutil

fol = ("C:\\Users\\sumit\\Desktop\\data\\grocerystore\\supersstore")
temp = ("C:\\Users\\sumit\\Desktop\\data\\grocerystore\\supersstore\\Temp\\")
path = ("C:\\Users\\sumit\\Desktop\\ML trainng\\test1\\")
n = 0
for file in glob.glob("C:\\Users\\sumit\\Desktop\\data\\grocerystore\\supersstore\\*.csv"):
    data1 = pd.read_csv(file, index_col=0)
    print(len(data1))
    if len(data1) < 20:
        shutil.move(file, temp)
    else:
        da1 = os.path.basename(file)
        data1.to_csv(path+ da1, index=False , header=0, encoding='utf-8')
        n = n+1
        print(da1)

