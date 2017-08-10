#!/bin/env python
# encoding: utf-8

"""
    dolartoday.py

    Scraping dolar today page

    Created by Michel Betancourt on 2017.
    Copyright (c) 2017 MIT. All rights reserved.
"""


import re
import fontawesome as fa
from requests import get

USD = fa.icons['usd']
EUR = fa.icons['eur']

def main():
    data = str(get('https://dolartoday.com/').content)
    money = re.findall(r'Bs. ([\d,]+)', data)

    print(f"{USD}: {money[0]}, {EUR}: {money[1]}")


if __name__ == '__main__':
    main()
