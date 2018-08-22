#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

__author__ = 'slucius'



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def printFromTopToBottom(self, root):
        # self.result = []
        # if not root:
        #     return None
        # self.result.append(root.val)
        # l = root.left
        # r = root.right
        #
        # while True:
        #
        #     if l:
        #         self.result.append(l.val)
        #         # l = root.left
        #     elif r:
        #         self.result.append(r.val)
        #         # r = root.right
        #     if l.left:
        #         l = l.left
        #
        #     # if not l:
        #     #     l = None
        #     # if not r:
        #     #     r = None
        #     if l.right:
        #         r = l.right
        #
        #     if r == None and r == None:
        #         break
        #
        # return self.result

    def PrintFromTopToBottom(self, root):
        if not root:
            return None

        currentStack = [root]
        res = []
        while currentStack:
            nextStack = []
            for i in currentStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                res.append(i.val)
            currentStack = nextStack
        return res


    '''引入一个队列即可。推广：有向图的广度优先遍历也是基于队列的。'''

    def PrintFromTopToBottom1(self, root):
        if not root:
            return []

        result = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            currentRoot = queue.pop(0)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
            result.append(currentRoot.val)

        return result

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
print(s.PrintFromTopToBottom1(pNode1))
print(s.PrintFromTopToBottom(pNode1))