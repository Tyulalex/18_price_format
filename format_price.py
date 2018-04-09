import re
import argparse


def format_price(price):
    price_str = str(price).strip()
    match_price = re.match(r'^\d+(\.\d*)?$', price_str)
    if match_price:
        price = '{:.2f}'.format(float(price))
        if re.match(r'^\d+\.00$', price):
            format_pattern = '{:,.0f}'
        else:
            format_pattern = '{:,}'
        return format_pattern.format(float(price)).replace(',', ' ')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--price', help='Price to be displayed in a nicely format')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(format_price(price=args.price))
