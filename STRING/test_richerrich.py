#!/bin/usr/env python3
from richerich import richieRich

def test_case1():
    assert richieRich('3943', 4,1) == '3993'

def test_case2():
    assert richieRich('092282', 6, 3) == '992299'

def test_case3():
    assert richieRich('0011', 4, 1) == '-1'

def test_case4():
    assert richieRich('12321', 5, 1) == '12921'

def test_case5():
    assert richieRich('932239', 6, 2) == '992299'
