import parsing

import unittest

class ScannerTest(unittest.TestCase):
    pass

class CharacterTest(unittest.TestCase):
    def test_single_character(self):
        payload = 'a'
        index = 0
        line = 0
        column = 0
        text = 'a'
        c = parsing.Character(payload=payload, index=index, line=line,
                              column=column, text=text)
        self.assertEqual(c.payload, payload)
        self.assertEqual(c.index, index)
        self.assertEqual(c.line, line)
        self.assertEqual(c.column, column)
        self.assertEqual(c.text, text)

if __name__ == "__main__":
    unittest.main()
