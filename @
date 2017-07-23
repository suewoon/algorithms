#!/usr/bin/env python3
#solution for https://www.acmicpc.net/problem/6603

from sys import stdin

class Selection:
    def __init__(self):
        pass

    def nCr(sets, n):
        if n == 0 :
            yield []
        else :
            for i in range(len(sets)):
                for c  in nCr(sets[i+1:], n-1) :
                    yield [sets[i]]+c

if __name__ == '__main__' :
    while True:
        line  = stdin.readline()
        if line == '':
            break
        arr = input_.split()
        k = int(arr[0])
        if k!=0 :
            s = Selection()
            for i in s.nCr(arr[1:],6) : print(' '.join(i))  #select 6 integer 
            print()



