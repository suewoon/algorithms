#/usr/bin/env python3 
# solution for https://www.hackerrank.com/challenges/coin-change

from functools import lru_cache
def get_ways(n, c):
    @lru_cache(maxsize=32)
    def get_ways_helper(n, m):
        if n < 0:
            return 0
        if n == 0:
            return 1

        if m<=0 and n>=1:
            return 0
        return get_ways_helper(n, m-1) + get_ways_helper(n-c[m-1], m)

    return get_ways_helper(n, len(c))


def main():
    n, m = tuple([int(x) for x in input().split()])
    c = [int(x) for x in input().split()]
    print(get_ways(n, c))

if __name__ == '__main__':
    main()

