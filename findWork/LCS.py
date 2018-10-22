#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 最长公共子序列 (The Longest Common Subsequence)
'''

__author__ = 'slucius'


def find_lcs(s1, s2):
    m = [[0 for x in range(len(s2) + 1)]  for y in range(len(s1) + 1)]
    d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                m[p1+1][p2+1] = m[p1][p2] + 1
                d[p1+1][p2+1] = 'ok'

            elif m[p1+1][p2] > m[p1][p2+1]:
                m[p1+1][p2+1] = m[p1+1][p2]
                d[p1 + 1][p2 + 1] = 'left'
            else:
                m[p1 + 1][p2 + 1] = m[p1][p2+1]
                d[p1 + 1][p2 + 1] = 'up'

    (p1, p2) = (len(s1), len(s2))
    print(d)


    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        if c == 'ok':
            s.append(s1[p1-1])
            p1 -= 1
            p2 -= 1
        if c == 'left':
            p2 -= 1
        if c == 'up':
            p1 -= 1
    s.reverse()
    return ''.join(s)

print(find_lcs('567128', '125678'))