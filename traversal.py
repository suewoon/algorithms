#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:19:31 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/TRAVERSAL

preOrder 27 16 9 12 54 36 72
inOrder 9 12 16 27 36 54 72
postOrder 12 9 16 36 72 54 27
"""
class Node(object):
    
    def __init__(self,data):
        self.rightNode = None
        self.leftNode = None
        self.data = data
    
    def __str__(self):
        return self.data

class BST(object):

    def postOrderTraversal(self,preOrder,inOrder):
        if preOrder == [] : 
            return 
        rootVal = preOrder[0]
        idx = inOrder.index(rootVal)
        length = len(preOrder)
        self.postOrderTraversal(preOrder[1:1+idx], inOrder[0:idx])
        self.postOrderTraversal(preOrder[1+idx:length], inOrder[idx+1:length])
        print(rootVal,end=' ')

testcases = int(input())
for i in range(testcases):
    n = int(input())
    preOrder = [int(x) for x in input().split()]
    inOrder = [int(x) for x in input().split()]
    bst = BST() 
    print(bst.postOrderTraversal(preOrder,inOrder))

