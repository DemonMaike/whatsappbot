import requests
import DB
from datetime import datetime
import secret

# non stop loop
while True:
    # detected the date today
    d = datetime.today()
    time = datetime.now().time()
    # start def in idicated time
    if str(time)[:5] == '20:15': 
        dt = f'{d.month}, {d.day}'

        data = {"chatid":secret.idchat, "message":f"{DB.name(dt)} c Днем рождения!"}

        #request for What's app API, url from green-api
        request = requests.post(secret.apiurl, json=data)
        print(request)
        print(secret.apiurl)
        time.sleep(3)
    
