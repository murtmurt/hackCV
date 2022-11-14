import requests
import time
import os, glob

files = glob.glob('frames\*')
for f in files:
    os.remove(f)

url1 = "https://facespacefaas.azurewebsites.net/api/update?"

dictionary = {
				"timestamp": round(time.time()),
				"popChange": 50,
				"avgROC": 0
			}

req = requests.post(url1, json = dictionary)
print(req.text)