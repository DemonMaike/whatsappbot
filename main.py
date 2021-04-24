import requests
import DB
from datetime import datetime
import secret

# non stop loop
while True:
    # detected the date today
    now = datetime.now()
    date_mounth = now.strftime('%m')
    date_day = now.strftime('%d')
    time = now.strftime('%H%M')
    print (time)
    # start def in idicated time
    if time == '20:15': 
        dt = f'{date_mounth}, {date_day}'

        data = {"chatid":secret.idchat, "message":f"{DB.name(dt)} c Днем рождения!"}

        #request for What's app API, url from green-api
        request = requests.post(secret.apiurl, json=data)
        print(request)
        print(secret.apiurl)
        time.sleep(3)
    
