import re
import locale
import platform
import argparse


def format_price(price):
    if not isinstance(price, str or int or float):
        raise TypeError('Cannot convert {} into integer'.format(type(price)))
    price_str = str(price).strip()
    if not re.match(r'\d+\.?\d*', price_str):
        raise ValueError('Cannot convert {} into integer'.format(price_str))
    locale_to_set = 'rus' if platform.system() == 'Windows' else 'ru_RU'
    locale.setlocale(locale.LC_ALL, locale_to_set)
    return locale.format(
        '%d', int(float(price_str)), grouping=True).replace(u'\xa0', ' ')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--price', help='Price to be displayed in a nicely format')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(format_price(price=args.price))
