#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'

class Node(object):
    '''Represents a singly linked Node.'''

    def __init__(self, data, next = None):
        self.data = data
        self.next = next




'''Test the Node class.'''
head = None
for count in range(1, 6):
    head = Node(count, head)
#print the contents of the structure.
#new build a pointer probe = head, called travelsal.
probe = head
while probe != None:
    print(probe.data)
    probe = probe.next
