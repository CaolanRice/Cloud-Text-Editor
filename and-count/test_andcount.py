import unittest
from app import and_count

class TestAndCounter(unittest.TestCase):

    def test_andcounter(self):
        text = "and hjello blah AND have and nice day"
        result = and_count(text)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
