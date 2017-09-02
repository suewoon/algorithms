#!/usr/bin/env python3 
# solution for https://www.acmicpc.net/problem/2839

class Packing(object):
    def __init__(self):
        self.weights = [3, 5]

    def measure(self, w_to_measure):
        memo = {}
        def measure_helper(n, remaining):
            if remaining in memo:
                return memo[remaining]
            elif remaining == 0:
                return n
            elif remaining < 2:
                return float('inf')
            else:
                ans = min(measure_helper(n+1, remaining-self.weights[0]), measure_helper(n+1, remaining-self.weights[1])) 
                if((remaining not in memo) or memo[remaining]>ans):
                    memo[remaining] = ans
                    print(memo)
                return ans

        measure_helper(0, w_to_measure)
        if memo[w_to_measure] == float('inf'):
            return -1
        else:
            return memo[w_to_measure]

def main():
    packing = Packing()
    print(packing.measure(int(input())))

if __name__ == '__main__':
    main()
