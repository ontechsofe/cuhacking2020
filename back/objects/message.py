from time import time

class Message(object):
    def __init__(self, text, session, sender, recipient, widget=None):
        self.text = text
        self.session = session
        self.sender = sender
        self.recipient = recipient
        self.time = int(time() * 1000)
        self.widget = widget