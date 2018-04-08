import re
import argparse


def format_price(price):
    price_str = str(price).strip()
    if re.match(r'^\d+(\.\d*)?$', price_str):
        return '{:,}'.format(int(float(price_str))).replace(",", " ")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--price', help='Price to be displayed in a nicely format')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(format_price(price=args.price))
