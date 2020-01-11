from flask import Flask, request
from hashlib import sha256
from json import dumps

messages = list()

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello World!'

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    messages.append(data['message'])
    hashed = sha256(dumps(messages).encode())
    state = {
        'state': hashed.hexdigest()
    }
    return state

@app.route('/messages', methods=['GET'])
def get_messages():
    resp = {
        'messages': messages
    }
    return resp

if __name__ == '__main__':
    app.run(debug=True)