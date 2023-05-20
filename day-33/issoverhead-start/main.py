import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -1.249970 # Your latitude
MY_LONG = 36.685459 # Your longitude
EMAIL = 'nipsalvin"gmail.com'
PASSWORD = ''


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    # if iss_latitude >= MY_LAT -5 and iss_latitude <= MY_LAT +5 and iss_longitude >= MY_LONG -5 and iss_longitude <= MY_LONG +5 :
    if MY_LAT-5 >= iss_latitude <= MY_LAT+5 and MY_LONG-5 >= iss_longitude <= MY_LONG+5:
        return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset:
        return True
    
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs='amwaniki.am"gmail.com',
                                msg='Subject:ISS is overhead\n\nLook to the sky')