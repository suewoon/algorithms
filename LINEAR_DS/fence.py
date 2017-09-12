#!/usr/bin/env python3
# solution for https://algospot.com/judge/problem/read/FENCE

class Fence(object):
    def __init__(self):
        pass

    def get_max_area(self, N, h):
            stack = []
            ret =0
            h.append(0)
            for i in range(N+1):
                while len(stack)>0 and h[stack[-1]] >= h[i]:
                    j = stack[-1]
                    stack.pop()
                    width = -1
            
                    if len(stack)==0:
                        width = i
                    else:
                        width = i - stack[-1] -1
                    ret = max(ret, h[j]*width)
                stack.append(i)
            return ret

def main():
    testcases = int(input())
    for i in range(testcases):
        N = int(input())
        h = [int(i) for i in input().split(' ')]
        fence = Fence()
        print(fence.get_max_area(N, h))

if __name__ == '__main__':
    main()
