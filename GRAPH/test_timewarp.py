#!/usr/bin/env python3

import pprint as pp
from graph.timewarp import *  

def test_case1():
    graph=Graph()
    for w in '0 1 1\n0 1 3'.split('\n'):
        graph.set_yrs_spent(w) 
    assert(get_time_change(graph.yrs_spent,0,2)[1]==1)
    assert(-get_time_change(graph.yrs_spent,0,2,True)[1]==3)

def test_case2():
    graph=Graph()
    for w in '0 2 -7\n0 3 -4\n3 2 9\n2 1 3'.split('\n'):
        graph.set_yrs_spent(w)
    assert(get_time_change(graph.yrs_spent,0,4)[1]==-4)
    assert(-get_time_change(graph.yrs_spent,0,4,True)[1]==8)

def test_case3():
    graph=Graph()
    for w in '0 2 0\n2 2 -1\n2 1 0'.split('\n'):
        graph.set_yrs_spent(w)
    print(graph.yrs_spent)
    # print(get_time_change(graph.yrs_spent,0,4)) 
    print(get_time_change(graph.yrs_spent,0,4,True)) 
    assert(get_time_change(graph.yrs_spent,0,4)[1]==0)



