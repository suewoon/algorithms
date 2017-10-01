#!/bin/python3
# https://www.hackerrank.com/challenges/richie-rich/problem


def richieRich(s, n, k):
    has_changed = [False]*n
    # make palindrome
    s = map(int, s)
    str_list = list(s)
    for i in range(n//2):
        if str_list[i] < str_list[-i-1]:
            str_list[i] = str_list[-i-1]
            has_changed[i] = True
            k -= 1
        elif str_list[i] > str_list[-i-1]:
            str_list[-i-1] = str_list[i]
            has_changed[-i-1] = True
            k -= 1

    if k < 0:
        return '-1'
    elif k == 0:
        return ''.join(str(x) for x in str_list)
    
    i = 0
    while k>=0 and i<n/2:
        if str_list[i] == 9:
            i += 1
            continue
        if k >= 1 and (has_changed[i] or has_changed[-i-1]):
            str_list[i] = str_list[-i-1] = 9
            k -= 1
        elif k>= 2:
            #digits haven't changed 
            str_list[i] = str_list[-i-1] = 9
            k -= 2
        i += 1

    if n%2 == 1 and k>0: # after the loops still 
        str_list[n//2] = 9
    return ''.join(str(x) for x in str_list)

def main():
    n, k = tuple([int(x) for x in input().split()])
    s = map(int, input())
    result = richieRich(s, n, k)
    print(result)

if __name__ == '__main__':
    main()

