#/usr/bin/env python3 
# solution for https://www.hackerrank.com/challenges/coin-change

from functools import lru_cache
def get_ways(n, c):

    @lru_cache(maxsize=32)
    def get_ways_helper(n, m):
        table = [[ 0 for i in range(m)] for i in range(n+1)]

        for i in range(m):
            # base case: n==0 일때 return 1
            table[0][i] = 1

        for i in range(1, n+1):
            for j in range(m):
                x = table[i-c[i]][j] if i - c[j] >=0 else 0

        if n < 0:
            return 0
        if n == 0:
            return 1

        # c에서 index<0 이고 n은 다 못채웠을 때
        if m<=0 and n>=1:
            return 0

        #c[m-1] 이 들어간 경우와 아예 안들어 간 경우 
        return get_ways_helper(n, m-1) + get_ways_helper(n-c[m-1], m)

    return get_ways_helper(n, len(c))


def main():
    n, m = tuple([int(x) for x in input().split()])
    c = [int(x) for x in input().split()]
    print(get_ways(n, c))

if __name__ == '__main__':
    main()

