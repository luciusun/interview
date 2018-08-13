
#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


import time

def loopNumber(problemSize):
    count = 0
    while problemSize:
        count += 1
        problemSize = problemSize//2
    return count


for size in [1000, 2000, 4000, 10000, 100000]:
    print(loopNumber(size))


    #program time
    # start = time.time()
    # loopNumber(size)
    # end = time.time()
    # print(end - start)


    #cpu time
    start = time.clock()
    loopNumber(size)
    end = time.clock()
    print(end - start)