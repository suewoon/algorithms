#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/bonetrousle
from functools import lru_cache

@lru_cache(maxsize=32)
def solve(n, k, b):
    min_range = list(range(1, b+1))
    min_sum = sum(min_range)
    max_sum = sum(range(k, k-b, -1))
    if n < min_sum or n > max_sum:
        return [-1]

    d = (n-min_sum)//b
    r = (n-min_sum)%b
    ans = [d + x for x in min_range]
    for i in range(b-1, b-r-1, -1):
        ans[i] += 1 
    return ans
  
""" def main():
    trips = int(input())
    for i in range(trips):
        n, k, b = map(int, input().split())
        print(solve(n, k, b))

if __name__ == '__main__':
    main()
"""
