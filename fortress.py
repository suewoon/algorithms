#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:08:52 2017

@author: suewoonryu

solution for  : https://algospot.com/judge/problem/read/FORTRESS
"""
class Fortress(object):
    def __init__(self, dict):
        
        
    def maxBarriers(self):
        
    
testcases = int(input())
for i in range(testcases):
    n = int(input())
    dict = {}
    for j in range(n):
        (x,y,r)=tuple(int(k) for k in input().split())
        dict[(x,y)] = r 
    fortress = Fortress(dict)
    print(fortress.maxBarriers())
    
    