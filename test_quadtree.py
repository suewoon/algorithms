#!/usr/bin/env python3
# test for quadtree.py 

from quadtree import QuadTree

def test_case_1():
    string = 'w'
    qt = QuadTree(string)
    assert qt.up_side_down() == 'w'

def test_case_2():
    string = 'xbwwb'
    qt = QuadTree(string)
    assert qt.up_side_down() == 'xwbbw'


def test_case_3():
    string = 'xbwxwbbwb'
    qt = QuadTree(string)
    assert qt.up_side_down() == 'xxbwwbbbw'

