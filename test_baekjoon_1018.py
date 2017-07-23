from baekjoon_1018 import Board 
import pprint as pp

def test_create_board():
    board = Board(8, 8)
    for string in 'WBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBBBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW'.split('\n'):
        board.create_board(string)

def test_sum():
    board = Board(8,8) 
    assert board.sum([[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]])==32

def test_crop_board_1():
    board = Board(8, 8)
    for string in 'WBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBBBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW'.split('\n'):
        board.create_board(string)
    assert board.crop_board() == 1 



