#/usr/bin/env python3 
# solution for https://www.hackerrank.com/challenges/coin-change

from functools import lru_cache
def get_ways(n, c):
    '''
    return the number of ways to make n units out of the given c_0, ... c_m-1
    coins
    '''
    @lru_cache(maxsize=32)
    def get_ways_helper(n, m):
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

def get_ways2(n, c):
    '''
    Bottom-up approach
    '''
    m = len(c)
    table = [[0 for _ in range(m)] for _ in range(n+1)]
    
    # base case n == 0
    for i in range(m):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            table[i][j] = (table[i][j-1] if j-1>=0 else 0) \
                           + (table[i-c[j]][j] if i-c[j] >=0 else
                                           0)
    return table[n][m-1]


def main():
    n, m = tuple([int(x) for x in input().split()])
    c = [int(x) for x in input().split()]
    print(get_ways(n, c))

if __name__ == '__main__':
    main()

