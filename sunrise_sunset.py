import requests
from datetime import datetime

MY_LAT = 39.290386
MY_LNG = -76.612190

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0

}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters )

response.raise_for_status()

sunrise_hr = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr = response.json()["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise_hr)
print(sunset_hr)


time_now = datetime.now()
print(time_now.hour)