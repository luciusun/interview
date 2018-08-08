#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


class LFUCache(object):
    def __init__(self, mostNumber):
        self.mostNumber = mostNumber
        self.d = dict()
        self.l = list()


    def set(self, k, v):
        d[k] = {}
        d[k]['value'] = v
        d[k]['count'] = 1

        if(len(l) == self.mostNumber):
            self.d.pop(self.l.pop())

        self.l.append(k)
        print(self.l, self.d)


    def get(self, k):
        if not self.d.get(k, None):
            return -1
        self.d[k]['count'] += 1
        t = list(map(lambda n: (n, self.d[n]['count']), self.d))
        t.sort(key=lambda x:x[1], reverse=True)
        self.l = [i[0] for i in t]
        print(self.l, self.d)
        return self.d[k]['value']



