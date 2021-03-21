from flask import Flask , render_template , make_response , request , session
import requests
import DB
from datetime import datetime
import secret

app = Flask(__name__)
app.config['SECRET_KEY'] = "2af888e0942c476c4eaeab2880a9e3d3a1426acb86730c1bd60b6d339f2256b2"

@app.route("/")
def index():
    return render_template('index.html',data = DB.get_all())

@app.route("/secret_page_for_send")
def send_bd():
    # detected the date today
    d = datetime.today()
    time = datetime.now().time()
    # start def in idicated time 
    dt = f'{d.month}, {d.day}'

    data = {"chatid":secret.idchat, "message":f"{DB.name(dt)} c Днем рождения!"}

    #request for What's app API, url from green-api
    request = requests.post(secret.apiurl, json=data)
    print(request)
    print(secret.apiurl)
    return "Well"
    
app.run(debug=True)



