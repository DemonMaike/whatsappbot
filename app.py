from flask import Flask
import os


app = Flask(__name__)

@app.route('/start-test')
def start_test():
    os.environ["TEST"] = "TEST"
    return "ok"

@app.route('/end-test')
def end_test():
    os.environ["TEST"] = "UNDEF"
    return "ok"

app.run()
