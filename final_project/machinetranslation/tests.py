import unittest
from translator import english_to_french,french_to_english


class TestFrenchToEnglish(unittest.TestCase):
    
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_NoneToFrench(self):
        self.assertRaises(ValueError, lambda : english_to_french(None) )

class TestEnglishToFrench(unittest.TestCase):
    
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_NoneToEnglsh(self):
        self.assertRaises(ValueError, lambda :french_to_english(None))