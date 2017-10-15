#!/bin/env python
# encoding: utf-8

"""
    dolartoday.py

    Scraping dolar today page

    Created by Michel Betancourt on 2017.
    Copyright (c) 2017 MIT. All rights reserved.
"""

import sys
import json
from requests import get

import fontawesome as fa

MONEY = fa.icons['money']
DT = fa.icons['trademark']
TRAN = fa.icons['cc-paypal']

API = 'https://s3.amazonaws.com/dolartoday/data.json'

def main():
    text = get(API).text
    data = json.loads(text)['USD']
    string = []
    if 'e' in sys.argv or 'all' in sys.argv:
        tmp = MONEY + '  ' + str(data['efectivo']) + '  '
        string.append(tmp)

    if 'ec' in sys.argv or len(sys.argv) <= 1 or 'all' in sys.argv:
        tmp = MONEY + 'C ' + str(data['efectivo_cucuta']) + '  '
        string.append(tmp)

    if 'dt' in sys.argv or 'all' in sys.argv:
        tmp = DT + '  ' + str(data['dolartoday']) + '  '
        string.append(tmp)

    if 'tf' in sys.argv or 'all' in sys.argv:
        tmp = TRAN + '  ' + str(data['transferencia']) + '  '
        string.append(tmp)

    print(' '.join(string))


if __name__ == '__main__':
    main()
