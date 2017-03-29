#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:05:04 2017

@author: suewoonryu

solution for https://algospot.com/judge/problem/read/BST
"""
class Node(object):
    def __init__(self, left=None, right=None,data=None):
        self.left = left
        self.right = right
        self.data = data
    
    def __str__(self):
        return self.data
        
class BST(object):
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        if self.root is None :
            return Node(data)
        else : 
            return _insert(self, self.root, data)
    
    def _insert(self, node, data):
        if node is None :
            return Node(data)
        if node.data < data : 
            self._insert(node.left, data)
        else :
            self._insert(node.right, data)
        return node 
    
    def hasDup(self, tup):
        tree={}
        tree[tupe[2]] is None :
            
        
    def isBST: 
        
        
    
testcases = int(input())
for i in range(testcases):
    n = int(input())
    bst = BST()
    for i in range(n):
        (left, right, data) = tuple(int(x) for x in input().split())
        bst.insert(data)
        tree[data] = (left,right)
    
