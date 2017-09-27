#!/usr/env/bin python3
# solution for https://www.hackerrank.com/challenges/sam-and-substrings


def make_substr2(string):
    ans = 0
    mod = (10**9 + 7)
    ones = 1

    for i in range(len(string)-1, -1, -1):
        ans += (int(string[i])*(i+1)*ones) % mod
        ones = (ones*10+1) % mod
    return ans%mod


def main():
    string = input()
    ans = make_substr2(string)
    print(ans)

if __name__ == '__main__':
    main()
