#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 23:15:26 2017
@author: suewoonryu
"""

class SnailProblem(object):
    """
    snail climbs out of a well. he climbs up 2m/day if it's rainy 
    or 1m/day if it's clear. 
    """
    
    def __init__(self, n, m):
        self.n = n #the well is n meter deep 
        self.m = m #the rainy season lasts for m days  
        assert(int==type(n) and int==type(m))
        self.cache = {}
        
    def getProb(self, days, howFar):
        
        if howFar >= self.n : 
            return 1 
        
        if days == self.m :
            return 0
        
        p = 0.75
        
        if (days,howFar) in list(self.cache.keys()) : 
            return self.cache[(days,howFar)]
        
        ans = p*self.getProb(days+1, howFar+2) + (1-p)*self.getProb(days+1, howFar+1)
        self.cache[(days,howFar)]= ans 
        return ans
        

testcase = int(input())
assert(int == type(testcase) and testcase <= 50 and testcase >= 1)
for i in range(testcase):
    (n,m)  = tuple(input().split())
    snailProblem = SnailProblem(int(n),int(m))
    print(snailProblem.getProb(0,0))


