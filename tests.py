import unittest
from datetime import datetime
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

    def test_incorrect_bool_type(self):
        self.assertEqual(None, format_price(True))

    def test_float_two_fixed_points(self):
        self.assertEqual('1 234.46', format_price(1234.45544))

    def test_incorrect_none_type(self):
        self.assertEqual(None, format_price(None))

    def test_incorrect_list_type(self):
        self.assertEqual(None, format_price([123456]))

    def test_incorrect_dict_type(self):
        self.assertEqual(None, format_price({'price': '4354354'}))

    def test_incorrect_tuple_type(self):
        self.assertEqual(None, format_price((3243243,)))

    def test_incorrect_datetime(self):
        self.assertEqual(None, format_price(datetime.now()))

    def test_not_match_string(self):
        self.assertEqual(None, format_price('123432,433'))

    def test_incorrect_type(self):
        self.assertEqual(None, format_price(b'1232343'))

    def test_many_zeros(self):
        self.assertEqual('3 000', format_price('3000.000000000000000000000000000000000000000000000000000000'))

