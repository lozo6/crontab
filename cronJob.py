import os
import time
import pandas as pd

# assign data to vairable
df = pd.read_csv('data/food_delivery.csv')

# get current time
currentTime = time.time()

# formats time into a string Year-Month-Day_Hour:Minute:Second
formatTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(currentTime))

# check cwd
cwd = os.getcwd()

# save data into new .txt file
with open(cwd + '/cronJob_' + formatTime + '.txt', 'w') as f:
    f.write(str(df))