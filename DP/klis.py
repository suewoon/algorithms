#!/usr/bin/env python3
# solution for https://algospot.com/judge/problem/read/KLIS

class KLIS(object):
    def __init__(self, arr):
        self.N = arr[0]
        self.K = arr[1]

    def read_input(self, _list):
        self.list = [int(i) for i in _list.split(' ')]



def main():
    testcases = int(input())
    for i in range(testcases):
        klis = KLIS([int(i) for i in input().split(' ')])
        klis.read_input(input())

if __name__ == '__main__':
    main()
