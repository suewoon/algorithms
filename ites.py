#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:57:23 2017

@author: suewoonryu

solutions for : https://algospot.com/judge/problem/read/ITES

"""
import queue

class ITESProblem(object):
   
    def getSignal(self):
        an_0 = 1983
        yield an_0
        while True:
            nextVal = (an_0*214013+2531011)%(2**32)
            yield (nextVal%10000+1)
            an_0 = nextVal
    
    def countSubSeq(self,k,n):
        signal = self.getSignal() #genertator object 
        ans = 0
        signalSum =0
        subSeq = queue.Queue()
        
        for i in range(n):
            newSignal = next(signal)
            signalSum += newSignal
            subSeq.put(newSignal)
            
            while(signalSum>k):
                signalSum -= subSeq.get()
                
            if signalSum == k :
                ans+=1
                
        return ans 
        
        
testcases = int(input())
for i in range(testcases):
      (k,n) = tuple([ int(i) for i in input().split()])
      p = ITESProblem()
      print(p.countSubSeq(k,n))


