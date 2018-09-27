#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


import sys

# n = int(input())
# s = int(input())
n = 5
s = [2, 5, 4, 3, 1]


l = len(s)

result = []

for i in range(l-1):
    num = 0
    for j in range(i, l):
        if s[i] > s[j]:
            num += 1

    result.append(num)


r1 = sum(result)

max_index = result.index(max(result))


s[max_index] = 0

result = []
for i in range(l-1):
    num = 0
    for j in range(i, l):
        if s[i] > s[j]:
            num += 1

    result.append(num)

r2 = sum(result)

print(r2)
print(max_index+1)

