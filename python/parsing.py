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
