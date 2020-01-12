from secret.config import DB_CONFIG
from objects.sql import SQL
from objects.message import Message

from flask import Flask, request
from flask_cors import CORS
from hashlib import sha256
from json import dumps

# DB Items
sql = None

messages = list()

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return 'Hello World!'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        completed = sql.new_client(data['name'], data['username'], data['password'])
        if completed:
            return {'success': True}, 200
        else:
            return {'success': False}, 400
    except:
        return {'success': False}, 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        client = sql.login(data['username'], data['password'])
        if client:
            return {'clientID': client[0], 'success': True}, 200
        else:
            return {'clientID': None, 'success': False}, 400
    except:
        return {'clientID': None, 'success': False}, 400

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    m = Message(data['message'], 1)
    messages.append(vars(m))
    hashed = sha256(dumps(messages).encode('utf8'))
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
    sql = SQL(DB_CONFIG)

    app.run(debug=True)