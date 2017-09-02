#!/usr/bin/env python3 
# solution for https://www.acmicpc.net/problem/2839

class Packing(object):
    def __init__(self):
        self.weights = [3, 5]

    def measure(self, w_to_measure):
        cache = {}
        def measure_helper(n, remaining):
            if remaining in cache:
                return cache[remaining]

            if remaining <= 0:
                return n

            ans = min(measure_helper(n+1, remaining-self.weights[0]),
                       measure_helper(n+1, remaining-self.weights[1]))
            cache[remaining] = ans
            return ans
        return measure_helper(0, w_to_measure)


def main():
    packing = Packing()
    print(packing.measure(int()))

if __name__ == '__main__':
    main()
