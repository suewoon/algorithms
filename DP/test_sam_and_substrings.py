from sam_and_substrings2 import make_substr2

def test_case1():
    assert make_substr2('16') == 23

def test_case2():
    assert make_substr2('123') == 164

def test_case4():
    assert make_substr2('22') == 26
def test_case3():
    assert make_substr2('213676822290') == 546421488
