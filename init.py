import requests
import pandas as pd
from datetime import datetime


req = requests.get(
    "http://beta.boltiot.com/fetchFromTable?fields=time_stamp,hum&duration=month&deviceName=BOLT1351489&from=&to=")
data = req.json()

humd_data = []
date_data = []

for datetimestring, humd in data["data"]:
    # print time.strptime(datetimestring, '%a, %d %b %Y %H:%M:%S GMT')
    date_data.append(datetime.strptime(datetimestring, '%a, %d %b %Y %H:%M:%S GMT'))
    humd_data.append(humd)

df = pd.DataFrame({"Humidity": pd.Series(humd_data, index=date_data)})
print df
