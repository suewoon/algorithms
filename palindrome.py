#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 10:59:25 2017

@author: suewoonryu

https://www.acmicpc.net/problem/1695
12135 
"""

import sys
sys.setrecursionlimit(10000)
#---> 왼쪽 오른쪽 번갈아서 떼보고 최소값을 리턴 
#def make_palindrome(seq,count):
#    if len(seq) < 2  : return count 
#    if seq[0] != seq[-1] : 
#        count+=1
#        seq.append(seq[0])
#    return make_palindrome(seq[1:-1],count)

def make_palindrome(seq,count):
    if len(seq)< 2 : return count 
    if seq[0]==seq[-1]:
        return make_palindrome(seq[1:-1],count)
    else :
        return min(make_palindrome(seq[1:],count),make_palindrome(seq[:-1],count))+1

if __name__=='__main__':
    n = int(input())
    count = 0
    seq = [int(x) for x in input().split()]
    print(make_palindrome(seq,count))