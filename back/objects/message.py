from time import time

class Message(object):
    def __init__(self, text, session, sender, recipient, sentiment, widget=None):
        self.text = text
        self.session = session
        self.sender = sender
        self.recipient = recipient
        self.time = int(time() * 1000)
        self.sentiment = sentiment
        self.widget = widget