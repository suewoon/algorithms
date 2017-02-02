# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 00:32:36 2017

@author: suewoonryu
"""
import sys 

def reverse(itr,compressedQt):
    head = next(itr)
    if(head == 'w' or 'b'):
        compressedQt = compressedQt[1:]
        return head 
    upperLeft = reverse(iter(list(compressedQt)), compressedQt)
    upperRight = reverse(iter(list(compressedQt[l])))
    lowerLeft = reverse()
    lowerRight = reverse()
    return str('x')+lowerLeft+lowerRight+upperLeft+upperRight
    

def main():
    testcases =sys.stdin.readline()
    for line in sys.stdin():
        print(reverse(iter(list(line)),line))

if __name__ == '__main__': main()