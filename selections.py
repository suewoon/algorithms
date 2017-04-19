#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:32:09 2017

@author: suewoonryu

combination & permutation 
https://goo.gl/VzXGJj -> nPr 

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

if __name__ == "__main__":
    print('Permutation : 4P2')
    for p in nPr(['a','b','c','d'],2): print(' '.join(p))
    print('Combination : 4C2 ')
    for p in nCr(['a','b','c','d'],2) : print(' '.join(p))
        