#!/usr/bin/env python3
# solution for https://algospot.com/judge/problem/read/MORSE

import math 

class Morse(object):
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k

    def n_of_cases(self, a, b):
        return math.factorial(a+b)//(math.factorial(a)*math.factorial(b))

    def k_th_code(self):
        ans = ''
        return self.k_th_code_helper(self.n, self.m, self.k, ans)

    def k_th_code_helper(self, n, m, k, ans):
        if n == 0 or m == 0:
            ans += '-'*n
            ans += 'o'*m
            return ans

        half_point = self.n_of_cases(n-1, m)
        print('n m k half ans', n, m, k, half_point, ans)
        if k > half_point:
            ans += 'o'
            return self.k_th_code_helper(n, m-1, k-half_point, ans)
        else:
            ans += '-'
            return self.k_th_code_helper(n-1, m, k, ans)


def main():
    testcases = int(input())
    for i in range(testcases):
        (n, m, k) = tuple(int(x) for x in input().split())
        morse = Morse(n, m, k)
        print(morse.k_th_code())


if __name__ == '__main__':
    main()

