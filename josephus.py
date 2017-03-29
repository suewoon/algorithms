#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:25:02 2017

@author: suewoonryu

solutions for : https://algospot.com/judge/problem/read/JOSEPHUS

"""
from llist import dllist

class JosephusProblem(object):
    def __init__(self, n,k):
        self.n = n
        self.k = k
        self.survivors = dllist([ str(i+1) for i in range(n)])

    def getSurvivors(self):
        i = 0 
        while self.survivors.size > 2 :
            node = self.survivors.nodeat(i)
            self.survivors.remove(node)
            i = (i+k-1)%(self.survivors.size)
        return list(self.survivors)


testcases = int(input())
for i in range(testcases):
    (n,k) = tuple([ int(i) for i in input().split()])
    p = JosephusProblem(n,k)
    print(' '.join(p.getSurvivors()))