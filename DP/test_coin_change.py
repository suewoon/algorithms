#!/usr/bin/env python3
# test for coin_change.py
from coin_change import get_ways


def test_case1():
    assert get_ways(10, [2,5,3,6]) == 5

def test_case2():
    get_ways(4, [1,2,3]) == 4

