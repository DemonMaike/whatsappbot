import requests
from data import name
from datetime import datetime
import secret

# non stop loop
while True:
    # detecting a date and time now
    now = datetime.now()
    time = now.strftime('%H:%M')
    date_now = now.strftime('%m-%d')

    # writeing a congretulation message in what's app in need time
    if time == '09:00': 

        data = {"chatid":secret.idchat, "message":f"{name(date_now)} c Днем рождения!"}

        #request for What's app API, url make from green-api
        request = requests.post(secret.apiurl, json=data)

        print(request)
        break
