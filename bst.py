#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 11:12:49 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/BST

"""


testcases = int(input())
for i in range(testcases):
    n = int(input())
    for j in range(n):
        #제일 먼저 루트를 찾는다. child에 포함이 안되는 것으로 
        (left,right,data) = tuple(int(x) for x in input.split())
        # data가 중복되서 들어오는 경우 생각 