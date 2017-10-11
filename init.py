import requests
import pandas as pd
from datetime import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='saxenakartik007', api_key='0OI5ZQTHcC6DXa885Gxs')

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


data = [go.Scatter(x=df.index, y=df.Humidity)]

layout_new = go.Layout(
    yaxis=dict(
        range=[20, 80]
    )
)

fig = go.Figure(data=data, layout=layout_new)

py.plot(fig, filename='axes-range-manual')