import unittest

from gender_converter import convert_gender


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual = convert_gender('f')
        expected = 'FEMALE'
        self.assertEqual(actual, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
