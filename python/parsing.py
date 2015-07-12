"""Module parsing contains classes used to implement a basic parser."""


class Character(object):
    """Class Character is a data object for a single character."""
    # pylint: disable-msg=too-few-public-methods
    def __init__(self, index, line, column, text):
        self.payload = text[index]
        self.index = index
        self.line = line
        self.column = column
        self.text = text

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Scanner(object):
    """Class Scanner is a scanner which reads in source text and then returns
    one character at a time in response to the 'get()' method."""

    def __init__(self, text):
        self.text = text
        self.index = 0
        self.line = 0
        self.column = 0

    def get(self):
        return Character(self.index, self.line, self.column, self.text)
