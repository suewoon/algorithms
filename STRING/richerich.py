#!/bin/python3
# https://www.hackerrank.com/challenges/richie-rich/problem

import sys

def richieRich(s, n, k):
    # Complete this function
    if n%2 == 0 :
        first_half = s[int(n/2):]
        second_half = s[:int(n/2)]
    else:
        first_half = s[int((n-1)/2):]
        second_half = s[:int((n-1)/2)]
    def make_palindrome(first_half, second_half, k):
        half_len = len(first_half)
        for i in range(half_len):
            if first_half[i] != second_half[half_len-i-1]:
                k -= 1 # k가 남아서 9로 바꿔주는 경우도 생각 .. 리스트 양쪽을 잘라내는 방법? 
                
                first_half[i] = second_half[half_len-i-1] = max(second_half[half_len-i-1],first_half[i])
        return first_half, k
    first_half, k = make_palindrome(list(first_half), list(second_half), k)
    if k ==0:
        second_half = first_half[:]
        first_half.reverse()
        return ''.join(str(x) for x in first_half+second_half)
    elif k<0:
        return -1

n, k = tuple([int(x) for x in input().split()])
s = input()
result = richieRich(s, n, k)
print(result)

