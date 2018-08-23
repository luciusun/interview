#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 树的几种遍历算法
'''

__author__ = 'slucius'



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution:
    def __init__(self):
        self.treenode = []


    '''(1)BST中序遍历'''

    def midTravelsal_in_BST1(self, pRoot):
        if len(self.treenode) < 0:
            return None

        if pRoot.left:
            self.midTravelsal_in_BST1(pRoot.left)
        self.treenode.append(pRoot)
        if pRoot.right:
            self.midTravelsal_in_BST1(pRoot.right)



    '''(2)BST中序遍历'''

    def midTravelsal_in_BST2(self, pRoot):
        if not pRoot:
            return None

        treeStack = []
        nodesQue = []
        pNode = pRoot
        while pNode or len(treeStack):
            while pNode:
                treeStack.append(pNode)
                pNode = pNode.left

            if len(treeStack):
                pNode = treeStack.pop()
                nodesQue.append(pNode)
                pNode = pNode.right
        return  nodesQue





