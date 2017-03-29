#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:13:50 2017

@author: suewoonryu

solutions for : https://algospot.com/judge/problem/read/BRACKETS2

"""
class Stack(object) : 
    def __init__(self):
        self.items = [] 
    
    def push(self, item): 
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return ''.join(self.items)

class MatchingBrackets(object):
    def __init__(self): 
        self.openbrackets = "({["
        self.closebrackets =  ")}]"
        self.stack = Stack()
    
    def pairOf(self, c):
        for i in range(3):
            if c == self.closebrackets[i]:
                return self.openbrackets[i]
    
    def isMatched(self, inputList):
        for c in inputList :       
            if c in self.openbrackets:
                self.stack.push(c)
            else : 
                if len(self.stack)!=0 and self.pairOf(c) == self.stack.pop(): 
                    continue 
                else :
                    return False 
        
        if len(self.stack) == 0 : 
            return True 
    
    
testcases = int(input())
for i in range(testcases):
    inputList = input()
    matchingBrackets = MatchingBrackets()
    if matchingBrackets.isMatched(inputList) : 
        print('YES')
    else : 
        print('NO')
    