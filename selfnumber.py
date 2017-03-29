#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:09:18 2017

@author: suewoonryu

solution for : https://www.acmicpc.net/problem/4673

"""

class SelfNumber(object):
    def __init__(self):
        self.arr = {}
        
    def get_d_n(self, n):
        d_n = n
        while n >= 1:
            d_n += n%10 
            n = int(n/10)
        return d_n
    
    def isSelfNumber(self,n): 
        self.arr[n]=True
        
    def printSelfNumber(self):
        n = 1
        while n < 10000: 
            d_n = self.get_d_n(n)
            if n!=d_n : 
                self.isSelfNumber(d_n)
            if n not in self.arr.keys():
                    print(n)
            n+=1 
         
selfNumber = SelfNumber()
selfNumber.printSelfNumber()