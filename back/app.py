from secret.config import DB_CONFIG, AI_ID
from objects.sql import SQL
from objects.message import Message

from flask import Flask, request
from flask_cors import CORS
from hashlib import sha256
from json import dumps

# DB Items
sql = None

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

@app.route('/start', methods=['POST'])
def start():
    data = request.get_json()
    try:
        session = sql.new_session(data['clientID'])
        if session:
            return {'sessionID': session[0], 'success': True}, 200
        else:
            return {'sessionID': None, 'success': False}, 400
    except:
        return {'sessionID': None, 'success': False}, 400

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    
    try:
        messageClient = Message(data['message'], data['sessionID'], data['clientID'], AI_ID)
        print(data)
        completed0 = sql.message(vars(messageClient))
        print(messageClient)
        print(completed0)
        # HANDLE ANALYZING THE MESSAGE HERE AND SEND A MORE COMPLEX ONE BELOW
        messageAI = Message('A better message will go here later.', data['sessionID'], AI_ID, data['clientID'])
        completed1 = sql.message(vars(messageAI))

        if completed0 and completed1:
            return {'success': True}, 200
        else:
            return {'success': False}, 400
    except:
        return {'success': False}, 400

@app.route('/messages', methods=['POST'])
def get_messages():
    data = request.get_json()
    try:
        messages = sql.get_messages(data['sessionID'])
        if messages:
            return {'messages': messages, 'success': True}, 200
        else:
            return {'messages': None, 'success': False}, 400
    except:
        return {'messages': None, 'success': False}, 400

if __name__ == '__main__':
    sql = SQL(DB_CONFIG)

    app.run(debug=True)