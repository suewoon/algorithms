#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:25:02 2017

@author: suewoonryu

solutions for : https://algospot.com/judge/problem/read/JOSEPHUS

"""

class JosephusProblem(object):
    def __init__(self):
        pass
            
    def get_survivors(self, n, k):
        def solution(arr, k, last_idx):
            if len(arr) <= 2:
                return arr
            arr.pop(last_idx)
            next_idx = last_idx + k - 1
            if next_idx >= len(arr):
                next_idx %= len(arr)
            return solution(arr, k, next_idx)
        return solution([(i+1) for i in range(n), k, 0)
                                             
                                             
def main():
    testcases = int(input())
    for i in range(testcases):
    (n,k) = tuple([ int(i) for i in input().split()])
    p = JosephusProblem()
    last_two = p.get_survivors(n,k)
    print(' '.join(str(x) for x in last_two))
                                             
if __name__ == '__main__':
                         main()
