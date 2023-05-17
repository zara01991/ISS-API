import requests
from datetime import datetime
import smtplib as smtp
import time
#import numpy
#pip install requests


MY_LAT = 39.290386
MY_LNG = -76.612190
my_email = "zzq01991@gmail.com"
password = "tsavaienyxixycdl"

def is_iss_overhead():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    # if response.status_code == 404:
    #    raise Exception ("That resource does not exist.")
    # if response.status_code == 401:
    #    raise Exception ("You are not authorized to access this data.")

    response.raise_for_status()
    longitude= float(response.json()["iss_position"]["longitude"])
    latitude = float(response.json()["iss_position"]["latitude"])
    #iss_position = (longitude, latitude)
    #print(iss_position)

    #my_position = (MY_LAT,MY_LNG)

    distance = ((longitude - MY_LNG)**2 + (latitude - MY_LAT)**2)**0.5

    if distance <= 50:
        return True



def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0

    }

    response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters )

    response.raise_for_status()

    sunrise_hr = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hr = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])


# print(sunrise_hr)
# print(sunset_hr)

    time_now = datetime.now()
    now_hr = int(time_now.hour)

    if now_hr > sunset_hr:
        return True


#print(distance)

#while True:
    #time.sleep(60)
    if is_iss_overhead and is_night():

        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(from_addr = my_email, 
                                to_addrs = "godspeedzara@gmail.com", 
                                msg = f"Subject:ISS Coming!\n\nCheck out the ISS location! It's close to you!.")

    else:
        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(from_addr = my_email, 
                                to_addrs = "godspeedzara@gmail.com", 
                                msg = f"Subject:ISS Moving\n\nKeep watching the ISS location.")