import os
import sys
import time
import pandas as pd

cwd = os.getcwd()

df = pd.read_csv('data/food_delivery.csv')

now = time.time()

nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

with open(cwd + '/cronJob_' + nowStr + '.txt', 'w') as f:
    f.write(str(df))