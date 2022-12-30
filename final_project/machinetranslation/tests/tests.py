import unittest
from .. import translator


class TestFrenchToEnglish(unittest.TestCase):
    
    def test_englishToFrench(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hello')
    def test_NoneToFrench(self):
        self.assertEqual("", translator.english_to_french(None) )

class TestEnglishToFrench(unittest.TestCase):
    
    def test_frenchToEnglish(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(translator.french_to_english('Bonjour'), 'Bonjour')

    def test_NoneToEnglsh(self):
        self.assertEqual("", translator.french_to_english(None))