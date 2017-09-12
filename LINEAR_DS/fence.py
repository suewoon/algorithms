#!/usr/bin/env python3
# solution for https://algospot.com/judge/problem/read/FENCE

class Fence(object):
    def __init__(self, N, h):
        self.N = N
        self.h = h

    def get_max_area(self):
        max_area = [0]*self.N
        def get_max_width(i, last_h):
            if i >= self.N-1 :
                return 1
            if self.h[i+1] < last_h:
                return 1
            else:
                return get_max_width(i+1, last_h)+1
        for i in range(self.N):
            max_area[i] = self.h[i]*get_max_width(i, self.h[i])
        return max(max_area)

def main():
    testcases = int(input())
    for i in range(testcases):
        N = int(input())
        h = [int(i) for i in input().split(' ')]
        fence = Fence(N, h)
        print(fence.get_max_area())

if __name__ == '__main__':
    main()
