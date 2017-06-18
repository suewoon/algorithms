#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 21:49:23 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/TIMETRIP
"""
import sys 
import math
input = sys.stdin.readline 

class Graph(object):
    def __init__(self,g):
        self.spent_yrs = [[math.inf for _ in range(g)] for _ in range(g)]
        for i in range(g):
            self.spent_yrs[i][i] = 0
                          
    def set_spent_yrs(self,a,b,d):
        self.spent_yrs[a][b] = d
    
if __name__=='__main__':
    testcases = int(input())
    for case in range(testcases): 
        (g,w) = tuple(int(x) for x in input().split())
        graph = Graph(g)
        for wormhole in range(w):
            #a:start , b:end, d:yrs time traveled through wormhole
            (a,b,d) = tuple(int(x) for x in input().split())
            
        

