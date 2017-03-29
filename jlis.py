# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 10:46:31 2017

@author: suewoonryu
"""
class JLIS(object):
    
    def getJlis(idxA, idxB):
        """
    
        :param idxA: starting index of sequence A
        :param idxB: starting index of sequence B
        :return: length of the joined longest increasing subsequence by A and B
        """
    



testcases = int(input())
for i in range(testcases):
    lengths  = [ int(j) for j in input().split()]
    lenA = lengths[0] 
    lenB = lengths[1]
    seqA= [ int(j) for j in input().split()]
    seqB = [int(j) for j in input().split()]
    cache = [[-1]*lengths[0] for j in range(lengths[1])]
    #print(seq)
    print(getJlis(0,0))