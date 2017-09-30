#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/bonetrousle
from functools import lru_cache


def select(n, b, k):
    if b == 0:
        return [[]]
    return [[x] + suffix for i, x in enumerate(k) 
            for suffix in select(n, b-1, k[i+1:]) if x <= n]


@lru_cache(maxsize=32)
def solve(n, k, b):
    if n > sum(list(range(1, k+1))):
        return '-1'
    for combination in select(n, b, list(range(k, 0, -1))):
        print(combination)
        if sum(combination) == n:
            break 
        else:
            combination = [-1]
    return ' '.join(str(x) for x in combination)


""" def main():
    trips = int(input())
    for i in range(trips):
        n, k, b = map(int, input().split())
        print(solve(n, k, b))

if __name__ == '__main__':
    main()
"""
