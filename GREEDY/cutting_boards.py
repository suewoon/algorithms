#!/usr/local/bin python3
#  solution for https://www.hackerrank.com/challenges/board-cutting/problem

def get_min_cost(y_i, x_i, m, n):
    '''
    return the minimum cost for cutting board into 1*1 square
    y_i: cutting horizontally, 1 <= y_i <= m
    x_i: cutting vertically, 1 <= x_i <= 
    '''
    h = 0
    v = 0
    ans = 0 
    mod = (10**9 + 7)
    
    for i in range(m+n-2): # (m+n) loop돌면 y_i, x_i가 모두 '' 됨
        xMax = x_i[-1] if len(x_i) else -1
        yMax = y_i[-1] if len(y_i) else -1

        if yMax < xMax:
            # vertical cut 
            v += 1
            c = x_i[-1]
            x_i.pop()
            ans += (c*(h+1))%mod
            continue

        else:
            # horizontal cut 
            h += 1 
            c = y_i[-1]
            y_i.pop()
            ans += (c*(v+1))%mod
    
    return ans%mod


if __name__ == '__main__':
    testcases = int(input())
    for i in range(testcases):
        m, n = map(int, input().split())
        y_i = list(map(int, input().split()))
        x_i = list(map(int, input().split()))
        get_min_cost(sorted(y_i), sorted(x_i), m, n)

