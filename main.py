import requests
import DB
from datetime import datetime
import secret


# detected the date today
d = datetime.today()
dt = f'{d.month}, {d.day}'

data = {"chatid":secret.idchat, "message":f"{DB.name(dt)} c Днем рождения!"}

#request for What's app API, url from green-api
request = requests.post(secret.apiurl, json=data)
print(request)
print(secret.apiurl)

