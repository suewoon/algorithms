#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:45:34 2017

@author: suewoonryu

https://www.acmicpc.net/problem/2309
"""

SUM_OF_HEIGHTS = 100 
NUM_OF_DWARFS = 9 

def subset(soFar, rest, delta, fake):
    if rest==[]  :
        if len(soFar)==2 and sum(soFar) == delta :
                fake+=soFar
                return fake 
    else : 
        subset(soFar,rest[1:],delta,fake)
        soFar_copy = soFar[:]
        soFar_copy.append(rest[0])
        subset(soFar_copy, rest[1:],delta,fake)
       
        
if __name__ == '__main__': 
    heights = [] 
    for i in range(NUM_OF_DWARFS):
        heights.append(int(input()))
    summation = sum(heights)
    delta = summation - SUM_OF_HEIGHTS
  
    assert (delta>=0), "sum of heights of 9 dwarfs has to be positive"
    
    fake = []
    subset([],heights, delta,fake)
    real = sorted([ elem for elem in heights if elem not in fake])
    for elem in real : 
        print(elem)
           