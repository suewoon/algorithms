# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 06:31:29 2017

@author: suewoonryu
"""
import numpy as np

class pi(object): 
    def __init__(self, piList):
    """
    initialize a pi object 
    piList : 
    """
    self.piList = piList
    self.cache = {}
        
    def getDifficulty(self, subList):
    """    
    """
    if cache[int(''.join(subList))] : 
        return cache[int(''.join(subList))]
        
    #1 : all the same number 
    if np.all(np.diff(subList, 1) == 0) :
        return 1 
    
    #2 : monotonic increasing or decreasing 
    if np.all(np.diff(subList, 1) == 1) or not np.all(np.diff(subList,1) == -1) : 
        return 2 
    
    #3 : 두 수가 번갈아 나타날 때
    if np.all(abs(np.diff(subList,1)) == abs(subList[1]-subList[0])) : 
        return 4
    
    #5 : arithmetic sequence 
    if np.all(np.diff(subList, 2) == 0): #differenced twice 
        return 5
    
    return 10 
    

    def minDifficulty(self, list):   
    """
    return minumum difficulty of the given list 
    make the sublist of which length is 3 ~ 5 and calculate get the 
    difficulty then recursively call the function
    """
    ans = 0 
    for i in range(2,5):
        ans = min(getDifficulty(list[:i+1])+minDifficulty(list[i+1:]))
    return ans 
   
   
try:
    testcases = int(input())
    assert type(testcases) == int
    for i in range(testcases):
        piList = [int(i) for i in input().split()]
        #pi = input()
        print(minDifficulty(pi))
except TypeError: 
    print('Invalid Input Type')
    