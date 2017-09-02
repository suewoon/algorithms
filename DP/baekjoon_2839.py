#!/usr/bin/env python3 
# solution for https://www.acmicpc.net/problem/2839

import sys
sys.setrecursionlimit(1500)

class Packing(object):
    def __init__(self):
        self.weights = [3, 5]
    #memo{1:inf, 2:inf, 3:1, 4:inf, 5:1, 6:2, ...}
    def measure(self, w_to_measure):
        memo = {}
        def measure_helper(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 0 
            elif remaining < 2:
                return float('inf')
            else:
                ans = min(measure_helper(remaining-self.weights[0])+1, measure_helper(remaining-self.weights[1])+1)
                if remaining not in memo or memo[remaining] > ans:
                    memo[remaining] = ans
                return ans
        measure_helper(w_to_measure)
        print(memo)
        if memo[w_to_measure] == float('inf'):
            return -1
        else:
            return memo[w_to_measure]

def main():
    packing = Packing()
    print(packing.measure(int(input())))

if __name__ == '__main__':
    main()
