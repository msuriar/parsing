class Character(object):
    def __init__(self, index, line, column, text):
        self.payload = text[index]
        self.index = index
        self.line = line
        self.column = column
        self.text = text
