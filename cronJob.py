import os
import time
import pandas as pd
import requests as rq
import json

# assign data to vairable
api = rq.get('https://data.cms.gov/data-api/v1/dataset/f1a8c197-b53d-4c24-9770-aea5d5a97dfb/data')
api = api.json()
api = pd.DataFrame(api)
api.to_csv('data/opiodData.csv')

df = pd.read_csv('data/opiodData.csv')

# get current time
currentTime = time.time()

# formats time into a string Year-Month-Day_Hour:Minute:Second
formatTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(currentTime))

# check cwd
cwd = os.getcwd()

# save data into new .txt file
with open(cwd + '/cronJob_' + formatTime + '.txt', 'w') as f:
    f.write(str(df))