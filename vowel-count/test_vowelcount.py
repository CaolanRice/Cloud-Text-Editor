import unittest
from app import vowel_count

class TestAndCounter(unittest.TestCase):

    def test_vowelcounter(self):
        text = "and hjello blah AND have and nice day"
        result = vowel_count(text)
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()