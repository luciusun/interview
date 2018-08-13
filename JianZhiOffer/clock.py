#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'




def timeClock(l):
    l = list(l)
    h=10*int(l[0])+int(l[1])
    m=10*int(l[3])+int(l[4])
    s=10*int(l[6])+int(l[7])
    if(h>=24):
        h = h%10
    if(m>=60):
        m= m%10
    if(s>=60):
        s= s%10

    ss=[]
    for i in list([h, m, s]):
        x = i//10
        y= i%10
        ss.append(str(x))
        ss.append(str(y))
    for j in ss:
        str(j)
    print(ss)
    ss.insert(2,':')
    ss.insert(5,':')

    return ''.join(ss)

    # return ss
# print(timeClock('19:90:23'))

f = open('myClockfile.txt', 'r')
# line = 1
for line in f:
    if(len(line)>=4):
        print(timeClock(line))
