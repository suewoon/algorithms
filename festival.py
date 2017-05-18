#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:02:38 2017

@author: suewoonryu

123123 -> 3 ~ 6 

"""
def get_min_avg(rest,n,l,min_avg):
    for i in range(l,n):
        min_avg = min(sum(rest[:i])/i, min_avg)
    if len(rest)==l:
        print(min_avg)
        return min_avg
    get_min_avg(rest[1:],len(rest[1:]),l,min_avg)

if __name__=='__main__':
    testcases = int(input())
    for i in range(testcases):
        (n,l) = tuple([int(x) for x in input().split()])
        cost = [int(x) for x in input().split()]
        get_min_avg(cost,n,l,max(cost))