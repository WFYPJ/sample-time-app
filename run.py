from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def get_time():
    time = datetime.now(timezone("US/Eastern"))
    return time.strftime("%H:%M:%S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
