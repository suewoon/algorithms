#/usr/bin/env python3 
# solution for https://www.hackerrank.com/challenges/coin-change


def get_ways(n, c):
    def get_ways_helper(n, sub_sets):
        if n < 0:
            return 0
        if n == 0:
            print("matched", sub_sets)
            return 1
        ans = 0
        for coin in c:
            ans += get_ways_helper(n-coin, sub_sets+[coin])
        return ans

    return get_ways_helper(n, [])


def main():
    n, m = tuple([int(x) for x in input().split()])
    c = [int(x) for x in input().split()]
    print(get_ways(n, c))

if __name__ == '__main__':
    main()

