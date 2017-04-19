#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:48:03 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/POLY
"""

class Polynomio(object):
    def __init__(self,N):
        self.N = N
        self.cache = {} 
    
    def return_monotone(self, N, first):
        if N==first : return  1 
        else : 
            if (N,first) in self.cache.keys() : 
                return self.cache[N,first]
            else : 
                for second in range(1,N-first+1):
                    self.cache[N-first,second] = (first+second-1)*self.return_monotone(N-first, second)
                    return self.cache[N-first,second] 
    
    def get_monotone(self):
        for i in range(1,self.N+1):
            return self.return_monotone(self.N, i)
    
if __name__ == "__main__":   
    testcases = int(input())
    for i in range(testcases):
        N = int(input())
        p = Polynomio(N)
        print(p.get_monotone())