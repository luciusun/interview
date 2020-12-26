#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用法：python3 excel2txt.py 123.xlsx > 123.txt

import sys
import os
from openpyxl import load_workbook


def request_batch(input_fp):
    workbook = load_workbook(input_fp)
    booksheet = workbook.active
    rows = booksheet.rows

    for row in rows:
        line_items = [str(col.value) for col in row]
        print('\t'.join(line_items))

request_batch(sys.argv[1])


