# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 00:13:21 2017

@author: suewoonryu
"""
"""def match(pattern,file):
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
                    return match(pattern[i+1:])"""

# a,b is the index of string
def match(a,b):
    if a > len(pattern)-1 or b > len(file)-1:
        return False

    cache = [[False]*len(pattern) for i in range(len(file))]

    # print(cache)
    if cache(a,b) :
        return cache(a,b)
    else:a
        for i in range(len(pattern)):
            for j in range(len(file)):
                if pattern[i]=='?' or pattern[i]==file[j]:
                    ans = match(a+1,b+1)
                    cache[i][j] = ans
                    return ans
                elif pattern[i]=='*':
                    ans = match(a+1, b) or match(a, b+1)
                    cache[i][j] = ans
                    return ans
                else :
                     return False



def match(pattern, string):
   n = len(string)
   m = len(pattern)
   if m==0:
       return n==0
   cache =  [[False]*n for i in range(m)]
   cache[0][0] = 0 # empty pattern can match with empty string

   for i in range(1,n+1):
       for j in range(1,m+1):
           if pattern[j-1] =='*':
               cache[i][j] = cache[i][j-1] or cache[i-1][j]
           elif pattern[j-1]=='?' or (string[i-1] == pattern[j-1]):
                cache[i][j] = cache[i-1][j-1]
           else :
               cache[i][j] = False

    return cache[n][m]

    
testcases = int(input())
for i in range(testcases):
     pattern = input()
     nOfFiles = int(input())
     for j in range(nOfFiles):
         cache = []
         file = input()
         # if match(pattern, file) : print(file)
         if match(0,0):

             print(file)
