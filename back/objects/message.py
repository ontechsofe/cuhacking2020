from time import time

class Message(object):
    def __init__(self, text, sender, widget=None):
        self.text = text
        self.sender = sender
        self.time = int(time() * 1000)
        self.widget = widget