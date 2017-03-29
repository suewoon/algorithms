#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:11:24 2017

@author: suewoonryu

solution for https://algospot.com/judge/problem/read/NERD2
"""
class Node : 
    def __init__(self, data):
        self.left = None 
        self.right = None 
        self.data = data 
    
    
class NerdTree(object):
    def __init__(self, root=None):
        self.root = root 
        
    def insertNode(self):
        

testcases = int(input())
for i in range(testcases):
    n = int(input())
    dict = {}
    for j in range(n):
        (p,q) = tuple(int(x) for x in input().split())
        dict[j] = (p,q)
        tree = NerdTree(dict)
        print(tree.sumOfCandidates())