import requests 
from datetime import datetime

# detect for date today
d = datetime.today()
dt = f'{d.month}, {d.day}'

# testing DB
human = {
     "2, 1": "Первый",
     "2, 2": "Второй",
     "2, 3": "Третий"
         }

# logic the bot, if today date is birthday user's, then write name in message. im stupid
name = []
for date in human.keys():
    if dt == date:
        name.append(human[dt])


# Setting for bot message, chat id and text
    data = {
        "chatid":"79162149060@c.us",
        "message":f"{name[0]}, c днем рождения!"
    }

#request for What's app API
request = requests.post("https://api.green-api.com/waInstance7896/SendMessage/72aa39e3263a85b1d0125c7bde800136b63bfaa1c38ebb4135", json=data)
print(request)