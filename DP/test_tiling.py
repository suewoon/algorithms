from brick_tiliing import tiling

class test_class(object):
    def test_case1(self):
        ans = tiling(2, 4, [list('....'), list('....')])
        assert ans == 2

    def test_case2(self):
        ans = tiling(3, 4, [list('...'), list('.#.'), list('...')])
        assert ans == 4 

    def test_case3(self):
        ans = tiling(2, 2, [list('##'), list('##')])
        assert ans == 1 


