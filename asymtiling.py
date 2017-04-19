#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 05:14:22 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/ASYMTILING
"""

class ASymtiling(object):
    '''
    width*2인 직사각형 안에 안에 2*1또는 1*2인 타일로 채우기 
    memoization 안하면 max recursion 초과 
    '''
    def __init__(self):
        self.cache={}
        
    def tiling(self, width):
        if width in self.cache.keys() : 
            return self.cache[width]
        else : 
            if width <= 1 : 
                self.cache[width]= 1
                return 1
            else : 
                self.cache[width] = self.tiling(width-2)+ self.tiling(width-1)
                return self.cache[width]
    
    def deleteSymmetric(self,width):   
        if width == 2 : 
            return 2 
        elif width %2 == 0 : #짝수 일 때 
            return self.tiling(width/2)+self.tiling((width-2)/2)
        else : 
            return self.tiling((width-1)/2)
    
    def asymmetricTiling(self,width):
        return (self.tiling(width)-self.deleteSymmetric(width))%1000000007

#if __name__ == "__main__":   
#    testcases = int(input())
#    for i in range(testcases):
#        width = int(input())
#        t = ASymtiling()
#        print(t.asymmetricTiling(width))
