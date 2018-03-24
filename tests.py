import unittest
from format_price import format_price


class PriceFormatTestCases(unittest.TestCase):

    def test_int_string(self):
        self.assertEqual('1 234 567', format_price('1234567'))

    def test_float_string(self):
        self.assertEqual('1 234', format_price('1234.00000'))

    def test_integer(self):
        self.assertEqual('1 234 567', format_price(1234567))

    def test_float(self):
        self.assertEqual('1 234 567', format_price(1234567.0000))

    def test_float_string_with_spaces(self):
        self.assertEqual('2 345', format_price(' 2345.0000 '))

    def test_incorrect_type(self):
        with self.assertRaises(TypeError):
            format_price(True)

    def test_not_match_string(self):
        with self.assertRaises(ValueError):
            format_price('123432,433')

