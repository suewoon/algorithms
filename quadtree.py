# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 00:32:36 2017

@author: suewoonryu
"""
import sys 

def reverse(itr, compressedQt):
    head = next(itr)
    if (head == 'w' or head == 'b'):
        compressedQt = compressedQt[1:]
        return head 
    upperLeft = reverse(itr, compressedQt)
    upperRight = reverse(itr, compressedQt)
    lowerLeft = reverse(itr, compressedQt)
    lowerRight = reverse(itr, compressedQt)
    return str('x')+lowerLeft+lowerRight+upperLeft+upperRight

def main():
    testcases =sys.stdin.readline()
    for line in sys.stdin:
        print(reverse(iter(list(line[:-1])),line[:-1]))

if __name__ == '__main__': main()