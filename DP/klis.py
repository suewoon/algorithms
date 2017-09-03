#!/usr/bin/env python3
# solution for https://algospot.com/judge/problem/read/KLIS

class KLIS(object):
    def __init__(self, arr):
        self.N = arr[0]
        self.K = arr[1]

    def read_input(self, _list):
        self.list = [int(i) for i in _list.split(' ')]

    def return_lis(self):
        cache = [None]*self.N
        lis_arr =[[self.list[i]] for i in range(self.N)]

        def c(idx):
            if cache[idx] != None:
                return cache[idx]
            else:
                ans = 1
                for i in range(idx, self.N):
                    if self.list[idx] < self.list[i]:
                        ans = max(ans, c(i)+1)
                        lis_arr[idx].append(self.list[i])
                cache[idx] = ans
                return ans

        ans = []
        for i in range(self.N):
            ans.append(c(i))

        print(lis_arr)
        return ans


def main():
    testcases = int(input())
    for i in range(testcases):
        klis = KLIS([int(i) for i in input().split(' ')])
        klis.read_input(input())

if __name__ == '__main__':
    main()
