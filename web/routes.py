from web import app
import os

@app.route('/start-test')
def start_test():
    os.environ["TEST"] = "TEST"
    return "ok"

@app.route('/end-test')
def end_test():
    os.environ["TEST"] = "UNDEF"
    return "ok"