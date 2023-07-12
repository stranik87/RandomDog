from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello, World!'

    elif request.method == 'POST':
        update = request.get_json()
        print(update)
        return 'Got a POST request!'

