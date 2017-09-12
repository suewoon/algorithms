#!/usr/bin/env python3 

from boardcover import Board


def test_make_board_1():
    board = Board(3,7)
    for string in '#.....#\n#.....#\n##...##'.split('\n'):
        board.read_line(string)
    assert board.cover() == 0


def test_make_board_2():
    board = Board(3,7)
    for string in '#.....#\n#.....#\n##..###'.split('\n'):
        board.read_line(string)
    assert board.cover() == 2


def test_make_board_3():
    board = Board(8,10)
    for string in '##########\n#........#\n#........#\n#........#\n#........#\n#........#\n#........#\n##########'.split('\n'):
        board.read_line(string)
    assert board.cover() == 1514
