import unittest
from .. import translator


class TestFrenchToEnglish(unittest.TestCase):
    
    def test_englishToFrench(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
    
    def test_NoneToFrench(self):
        self.assertRaises(ValueError, lambda : translator.english_to_french(None) )

class TestEnglishToFrench(unittest.TestCase):
    
    def test_frenchToEnglish(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
    
    def test_NoneToEnglsh(self):
        self.assertRaises(ValueError, lambda :translator.french_to_english(None))