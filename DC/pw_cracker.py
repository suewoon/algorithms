#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/password-cracker
from sys import setrecursionlimit
setrecursionlimit(4000)

def parse(users, pass_arr, login_attempt):
    '''
    parse the given string,  login_attempt
    according to pass[0] - pass[n-1]
    if can't - return 'WRONG PASSWORD'
    '''
    def parse_(login_attempt, cur, cache):
        '''
        cur: current answer 
        cache: for memoization
        '''
        if len(login_attempt) == 0:
            return cur

        if login_attempt in cache:
            # return empty string since it has been concatenated to cur
            return ''

        for i in range(users):
            if login_attempt.startswith(pass_arr[i]):
                cur_ans = parse_(login_attempt[len(pass_arr[i]):], cur+' '+pass_arr[i], cache)
                if cur_ans != '':
                    return cur_ans

        cache.add(login_attempt)
        return ''

    return parse_(login_attempt, '', set([]))



if __name__ == '__main__':
    testcases = int(input())
    for i in range(testcases):
        users = int(input())
        pass_arr = input().split()
        login_attempt = input()
        ans = parse(users, pass_arr, login_attempt)
        print('WRONG PASSWORD' if ans == '' else ans)
