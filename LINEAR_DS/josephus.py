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
        last_two = []
        survivors = [(i+1) for i in range(n)]
        len = n-1
        idx = 0

        survivors.pop(idx)
        while len > 2:
            idx = (idx + k%len) % len -1 
            if idx == -1:
                idx += len
            survivors.pop(idx)
            len -= 1
        return survivors


def main():
    testcases = int(input())
    for i in range(testcases):
        (n,k) = tuple([ int(i) for i in input().split()])
        p = JosephusProblem()
        last_two = p.get_survivors(n,k)
        print(' '.join(str(x) for x in last_two))

if __name__ == '__main__':
    main()
