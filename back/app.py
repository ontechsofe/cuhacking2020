from secret.config import DB_CONFIG, MODEL_CONFIG, AI_ID
from objects.sql import SQL
from objects.model import Model
from objects.message import Message
from objects.responses import good_responses, bad_responses, start_conversation, start_conversation_responses

from flask import Flask, request
from flask_cors import CORS
from hashlib import sha256
from json import dumps
from random import randint

# Global Items
sql = None
model = None

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
        prediction = model.predict(data['message'])
        sentiment = None
        for annotation_payload in prediction:
                sentiment = annotation_payload.text_sentiment.sentiment

        messageClient = Message(data['message'], data['sessionID'], data['clientID'], AI_ID, sentiment)
        completed0 = sql.message(vars(messageClient))
        
        messageToClient = ""
        if data['message'] in start_conversation:
            messageToClient = start_conversation_responses[randint(0, 4)]
        elif (('thanks' in data['message'].lower()) or ('thank you' in data['message'].lower())):
            messageToClient = 'No problem! I\'m always here to help!'
        else:
            if sentiment == 1:
                messageToClient = good_responses[randint(0, 4)]
            else:
                messageToClient = bad_responses[randint(0, 4)]

        messageAI = Message(messageToClient, data['sessionID'], AI_ID, data['clientID'], sentiment)
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



# ALL FOR THERAPIST
@app.route('/clients', methods=['GET'])
def clients():
    try:
        clients = sql.get_clients()
        if clients:
            return {'clients': clients, 'success': True}, 200
        else:
            return {'clients': None, 'success': False}, 400
    except:
        return {'clients': None, 'success': False}, 400

@app.route('/client/messages', methods=['POST'])
def client_messages():
    data = request.get_json()
    try:
        messages, session_ids = sql.all_messages(data['clientID'])
        if messages:
            return {'messages': messages, 'sessionIDs': session_ids, 'success': True}, 200
        else:
            return {'messages': [], 'sessionIDs': [], 'success': False}, 200
    except:
        return {'messages': [], 'sessionIDs': [], 'success': False}, 200

if __name__ == '__main__':
    sql = SQL(DB_CONFIG)
    model = Model(MODEL_CONFIG)

    app.run(debug=False)