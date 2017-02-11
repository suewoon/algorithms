# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 00:48:59 2017

@author: suewoonryu
"""
    
def main():
    testcase = input()
    for i in range(0, 2*testcase, 2):
        member = input()
        fan = input()
        print(hug(member,fan))
        
if '__name__' == '__main__' : main()



def karatsuba(A,B) : 
    
    for i in len(A):
        for j in len(B):
            C
def hug(member,fan):
    #how many time they had a hug 
    hugs = 0 
    members = len(member)
    fans = len(fan)
    A = list(member)
    B = list(fan)
    
    C = karatsuba(A,B)
    for i in range(members-1, fans):
        if C[i] == 0 :
            hugs++
            
    return hugs 
        