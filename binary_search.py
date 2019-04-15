#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import random

def bs(arr, v):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = arr[mid]

        if guess == v:
            return mid

        if guess > v:
            high = high -1

        if guess < v:
            low = low + 1

    return None

arr = [1, 2, 3, 4, 5, 6, 9, 30, 221, 244, 332]

for i in range(1000000):
    bs(arr, random.randint(1, 332))

"""
python binary_search.py  2.97s user 0.06s system 99% cpu 3.048 total

感觉速度比php慢很多
"""
