#!/usr/local/bin python3
# sample solution 

from collections import Counter


def sorted_str(s):
    return ''.join(sorted(list(s)))


def solve(s):
    res = 0
    for l in range(1, len(s) + 1):
        a = [sorted_str(s[i:i+l]) for i in range(len(s) -l +1)]
        b = Counter(a)
        for _, v in b.items():
            res += v * (v-1) // 2
        return res 


t = int(input())
for _ in range(t):
    print(solve(input()))
