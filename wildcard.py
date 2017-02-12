# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:13:21 2017

@author: suewoonryu
"""
def match(pattern,file):
    if (pattern,file) in cache:
        return cache[(pattern,file)]
    else : 
        for i in range(len(pattern)):
            # match one by one 
            if pattern[i]!='*':
                if file[i]!=pattern[i] and pattern[i]!='?':
                    return False 
                cache[(pattern,file)] = ans 
                return match(pattern[i+1:],file[i+1:]) 
            # match one by many, pattern[i]=='*'
            else: 
                if file[i]==pattern[i+1]:
                    return match(pattern[],file[]) or match()
                else : 
                    return match(pattern[i+1:])
                    
        
    
testcases = int(input())
for i in range(testcases):
     pattern = input()
     nOfFiles = int(input())
     cache = {}
     for j in range(nOfFiles):
         file = input()
         if(match(pattern,file)):
             print(file)

     


         

    