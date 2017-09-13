#!usr/bin/env python3
# pytest for baekjoon_2579.py
from baekjoon_2579 import JumpGame

class Test_Class(object):
    def test_read_input(self):
        game = JumpGame(6)
        for s in '10\n20\n15\n25\n10\n20'.split('\n'):
            game.read_input(s)
        print(game.scores)
        #assert 0

    def test_max_final_score(self):
        game = JumpGame(6)
        for s in '10\n20\n15\n25\n10\n20'.split('\n'):
                        game.read_input(s)
        max_score = game.max_final_score()
        assert max_score == 75
