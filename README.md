# Price Formatter

Script formats price into human readable output
If function cannot parse input price, then **None** value returned
# System requirements

python version 3 installed


# How to run

1. Command line interface

```
python format_price.py --price 4323.0000
```

2. in the program

```python
from format_price import format_price
print(format_price(43232.0000))
```

# Tests

script is covered by unittest
to run them:

```
python tests.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
