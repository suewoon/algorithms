# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 00:31:34 2017

@author: suewoonryu
"""
class Quantization(object):
    def __init__(self, n):
        
def quantify(list):
    """
    quantify the given list by numOfQuantum 
    """

"""
1 <= test case <= 50
all the integers in seq are less than 1000 & greater than 0 
""""
testcases = int(input())
for i in range(testcases):
    info = [int(j) for j in input().split()]
    length = info[0]
    numOfQuantum = info[1]
    seq = [int(j) for j in input().split()]
    print(quantify(seq))
    