"""Tests for module 'parsing'."""

import parsing

import unittest


class ScannerTest(unittest.TestCase):
    """Unittests for Scanner class."""
    def test_single_character(self):
        text = 'b'
        testdata = [
            dict(index=0, line=0, column=0, text=text),
            ]

        s = parsing.Scanner(text=text)
        for i in range(len(text)):
            c = s.get()
            expected = parsing.Character(**testdata[i])
            self.assertEqual(c, expected)


class CharacterTest(unittest.TestCase):
    """Unittests for Character class."""
    def test_single_character(self):
        payload = 'a'
        index = 0
        line = 0
        column = 0
        text = 'a'
        c = parsing.Character(index=index, line=line, column=column, text=text)
        self.assertEqual(c.payload, payload)
        self.assertEqual(c.index, index)
        self.assertEqual(c.line, line)
        self.assertEqual(c.column, column)
        self.assertEqual(c.text, text)

if __name__ == "__main__":
    unittest.main()
