#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note:
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

__author__ = 'slucius'


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.father = None
        self.left = None
        self.next = None

#
# class Solution:
#     def getNext(self, pNode):
#         #case one
#         ppNode = pNode
#         if pNode == None:
#             return None
#
#         if ppNode.right != None:
#             while ppNode.right.left != None:
#
#                 ppNode.right = ppNode.right.left
#             return ppNode.right
#
#         #case two
#         ppNode = pNode
#         if ppNode.right == None and ppNode.father.left == ppNode:
#             return ppNode.father
#
#         #case three
#         ppNode = pNode
#         if ppNode.right == None and ppNode.father.right == ppNode:
#             while ppNode.father != ppNode.father.father.left:
#                 ppNode.father = ppNode.father.father
#             return ppNode.father.father.right



class Solution:
    def getNext(self, pNode):
        dummy = pNode
        while dummy.next:
            dummy = dummy.next

        self.result = []
        self.midTraversal(dummy)
        if self.result.index(pNode) != len(self.result)-1:
            return self.result[self.result.index(pNode)+1]
        else:
            return None



    def midTraversal(self, root):
        if not root:
            return
        self.midTraversal(root.left)
        self.result.append(root)
        self.midTraversal(root.right)


'''
三种情况：当前节点有右子树的话，当前节点的下一个结点是右子树中的最左子节点；
当前节点无右子树但是是父节点的左子节点，下一个节点是当前结点的父节点；
当前节点无右子树而且是父节点的右子节点，则一直向上遍历，直到找到最靠近的一个祖先节点pNode，
pNode是其父节点的左子节点，那么输入节点的下一个结点就是pNode的父节点。
'''


class Solution2:
    def getNext(self, pNode):
        # 输入是一个空节点
        if pNode == None:
            return None
        # 如果输入节点有右子树，则下一个结点是当前节点右子树中最左节点
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode

        else:
            # 如果当前节点有父节点且当前节点是父节点的左子节点, 下一个结点即为父节点
            if pNode.next and pNode.next.left == pNode:
                return pNode.next
            # 如果当前节点有父节点且当前节点是父节点的右子节点, 那么向上遍历
            # 当遍历到当前节点为父节点的左子节点时, 输入节点的下一个结点为当前节点的父节点
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                # 遍历终止时当前节点有父节点, 说明当前节点是父节点的左子节点, 输入节点的下一个结点为当前节点的父节点
                # 反之终止时当前节点没有父节点, 说明当前节点在位于根节点的右子树, 没有下一个结点
                if pNode.next:
                    return pNode.next























