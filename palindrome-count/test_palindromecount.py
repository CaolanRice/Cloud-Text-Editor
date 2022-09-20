import unittest
from app import palindrome_count

class TestPalindromeCounter(unittest.TestCase):

    def test_palindromecounter(self):
        text = "anna and her mum are driving their racecar to racecar land"
        result = palindrome_count(text)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
