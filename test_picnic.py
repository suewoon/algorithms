#!usr/bin/env python3 
#pytest for picnic.py

from picnic import MakingPairs

def test_count_pairs_1():
    mp = MakingPairs(2,[0,1])
    assert(mp.count_pairs() == 1)

def test_count_pairs_2():
    mp = MakingPairs(4,[0,1,1,2,2,3,3,0,0,2, 1,3])
    assert(mp.count_pairs() == 3)

def test_count_pairs_3():
    mp = MakingPairs(6, [0, 1, 0, 2, 1, 2, 1, 3, 1, 4, 2, 3, 2, 4, 3,  4,3,5,4, 5])
    assert(mp.count_pairs() == 4)




