#!/usr/bin/env python3
# solution for https://www.acmicpc.net/problem/2579

class JumpGame(object):
    def __init__(self, N):
        self.scores = [0]
        self.N = N

    def read_input(self, _input):
        self.scores.append(int(_input))

    def max_final_score(self):
        memo = {}

        def max_score_helper(start):
            if start in memo:
                return memo[start]

            if start == self.N:
                return self.scores[self.N]
            elif start == self.N-1:
                return self.scores[self.N] + self.scores[self.N-1]
            elif start == self.N-2:
                return self.scores[self.N] + self.scores[self.N-2]

            ans = max(max_score_helper(start+1), max_score_helper(start+2)) + self.scores[start]
            memo[start] = ans
            return ans
        print(memo)
        return max(max_score_helper(0), max_score_helper(1))

def main():
    N = int(input())
    game = JumpGame(N)
    for i in range(N):
        game.read_input(input())  #score of each step in the stair
    print(game.max_final_score())



if __name__ == '__main__':
    main()
