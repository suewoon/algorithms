#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:32:09 2017

@author: suewoonryu

combination & permutation : exhaustive recursion

"""

def nPr(sets, n):
    #assert n>=0 and n<=len(sets), "cannot choose more than set has"
    if n==0 : yield [] 
    else :
        for i in range(len(sets)):
            for c in nPr(sets[:i]+sets[i+1:], n-1):
                yield [sets[i]]+c 
                      
def nCr(sets, n):
    #assert n>=0 and n<=len(sets), "cannot choose more than set has"
    if n==0 : yield [] 
    else :
        for i in range(len(sets)) : 
            for c in nCr(sets[i+1:], n-1):
                yield [sets[i]]+c 

def nPr_2(soFar, rest):
    if rest == [] : 
        print(soFar)
        return 
    else : 
        for i in len(rest) : 
            nPr_2(soFar+rest[i],rest[0:i]+rest[i:])

def nCr_2(soFar, rest):
    if rest == [] :
        print(soFar)
        return 
    else : 
        for i in len(rest):
            nCr_2(soFar+rest[0], rest[1:]) #include first char 
            nCr_2(soFar,rest[1:]) #exclude first char 
            
if __name__ == "__main__":
    print('Permutation : 4P2')
    for p in nPr(['a','b','c','d'],2): print(' '.join(p))
    print('Combination : 4C2 ')
    for p in nCr(['a','b','c','d'],2) : print(' '.join(p))
    