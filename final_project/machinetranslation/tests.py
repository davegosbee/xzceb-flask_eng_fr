import unittest
from translator import englishToFrench,frenchToEnglish


class TestFrenchToEnglish(unittest.TestCase):
    
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    def test_NoneToFrench(self):
        self.assertRaises(ValueError, lambda : englishToFrench(None) )

class TestEnglishToFrench(unittest.TestCase):
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    
    def test_NoneToEnglsh(self):
        self.assertRaises(ValueError, lambda :frenchToEnglish(None))