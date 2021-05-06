import unittest
from parse_log import open_file
class TestStringMethods(unittest.TestCase):
    def test_alpha(self):
        self.assertEqual(not 'Introduion'.isalpha(),False)
    def test_digit(self):
        self.assertEqual('1234'.isdigit(),True)
    def test_marks(self):
        self.assertEqual(not '$$@::!!$%'.isdigit()and not '$$@!!$%'.isalpha() ,True)
    def test_open_file(self):    
        self.assertTrue((open_file))



if __name__ == '__main__':
    unittest.main()