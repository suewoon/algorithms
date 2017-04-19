#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 08:16:07 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/DICTIONARY
"""
import string

error = 'INVALID HYPOTHESIS'

class Dictionary(object):
    def __init__(self):
        self.alphabet=string.ascii_lowercase
        self.newOrder={}
    
    def find_newOrder(self, words):
        for i in range(len(words)-1):
            for j in range(len(words[i])) :
                print('i: ',i,'j: ',j)
                if words[i][j] != words[i+1][j]:
                    self.newOrder[words[i][j]]=[words[i+1][j]]
                    break    
    
    def is_aphabetical_order(self,char_list):
        return sorted(char_list) == char_list 
    
    def return_newOrder(self):
        '''
        DFS이용
        '''
        for i in self.newOrder.keys():
            if is_aphabetical_order(self.newOrder[i][0],self.newOrder[i][1]):
                pass 
            else : 
                self.alphabet.remove()
            
d = Dictionary() 
x=['gg',
'kia',
'lotte',
'lg',
'hanhw']
d.find_newOrder(x)  
#if __name__ == "__main__":
#    testcases = int(input())
#    for i in range(testcases):
#        d = Dictionary()
#        n = int(input())
#        words = []
#        for j in range(n):
#            words.append(str(input()))
       