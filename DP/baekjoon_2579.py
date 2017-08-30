#!/usr/bin/env python3
# solution for https://www.acmicpc.net/problem/2579

class JumpGame(object):
    def __init__(self, N):
        self.scores = [0]
        self.N = N

    def read_input(self, _input):
        self.scores.append(int(_input))

    def max_final_score(self):
        def max_score_helper(start, score):
            if start >=  self.N:
                return score
            score += self.scores[start]
            return max(max_score_helper(start+1, score),
                       max_score_helper(start+2, score))
        return max_score_helper(0, 0)

def main():
    N = int(input())
    game = JumpGame(N)
    for i in range(N):
        game.read_input(input())  #score of each step in the stair
    print(game.max_final_score())



if __name__ == '__main__':
    main()
