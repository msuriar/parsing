class Character(object):
    def __init__(self, payload, index, line, column, text):
        self.payload = payload
        self.index = index
        self.line = line
        self.column = column
        self.text = text
