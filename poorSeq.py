# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 22:38:27 2017

@author: suewoonryu
"""
class GoodSeqProblem(object):
    
    class Seq(object):
        def  __init__(self, N):
        """
        Initialize a sequence
        subList : list of integer, length of N 
        """
        assert type(N) == int 
        self.fullLength = N 
        self.seq = []
        
        def __str__(self):
            return ''.join(self.seq)
            
    def __init__(self, availableNums):
        self.availableNums = availableNums

    def getGoodSeq(self,N):
        mySeq = Seq(N)
        isGoodSeq = getGoodSeqUtil(mySeq)
        if isGoodSeq : 
            return mySeq 
    
    def getGoodSeqUtil(self, idx, seq):
        
        if len(mySeq.seq) == mySeq.fullLength : 
            return True
    
        for i in self.availableNums :
            isGood = True            
            
            for j in int(len(seq.seq)/2):
                if :
                    isGood=False
                    break
                
            if isGood:
                mySeq.seq.append(i)
                if getGoodSeqUtil(idx+1, seq):
                    return True
    
        return False 
            

goodSeqProblem = GoodSeqProblem([1,2,3])
goodSeq = goodSeqProblem.getGoodSeq(7)
print(goodSeq)

    
