#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 08:43:24 2017

@author: suewoonryu

solution for  https://algospot.com/judge/problem/read/NTHLON

Integer Programming 
"""
import sys 
import math
input = sys.stdin.readline


records=[]

def is_feasible(records):
    diff= []
    feasibility = True 
    for elem in records: 
        diff.append(math.copysign(1,elem[0]-elem[1]))    
    if abs(sum(diff)) == len(records):
        feasibility = False 
    return feasibility

def solve(records):
    return True

if __name__=='__main__':
    testcases = int(input())
    for i in range(testcases):
        n_of_events = int(input())
        for j in range(n_of_events):
            (a,b) = tuple( int(x) for x in input().split())
            records.append((a,b))
        print(solve(records) if is_feasible(records) else 'IMPOSSIBLE')


