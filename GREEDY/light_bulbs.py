#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/turn-off-the-lights/problem


def get_min_cost(c, k):
    leastCost = 1000*(10**9)
    n = len(c)
    # starting point can be index 0, 1, 2, ... k 
    # after that we jump 2k+1
    for i in range(k+1):
        if  n <= i:
            break 
        if ((n-1-i) % (2*k+1)) > k:
            continue 
        currSum = 0
        for j in range(i, n, 2*k+1):
            currSum += c[j]
        leastCost = min(lastCost, currSum)

    return leastCost

if __name__ == '__main__':
    n, k = map(int, input().split())
    c = list(int, input().split())
    print(get_min_cost(c, k))
