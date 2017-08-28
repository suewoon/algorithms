#!/usr/bin/env python3

class Reader(object):
    def __init__(self, words):
        self.words = words

    def read_input(self, _input, param):
        _list = [float(x) for x in _input.split(' ')
        def read_input_helper(_array, _list):
            if _array:
                _array.append(_list)
            else:
                 _array = [_list] 

        if param == 'first_pos_probs':
            read_input_helper(self.first_pos_probs, _list)
        elif param == 'cond_probs':
            read_input_helper(self.cond_probs, _list)
        elif param == 'classified_probs':
            read_input_helper(self.classified_probs, _list)

    def read_words(self, _input):
        ans = []
        for word in _input:
            if _input.index(word) == 0:
                 p = [ (p_ab/p_a) for p_a, p_ab in zip(self.first_pos_probs,
                                                      self.classified_probs[0]) if p_a!=0 ]
            else:
                 idx = self.words.index(word)
                 pre_idx = self.words.index(ans[-1])
                 p = [ (p_ab/p_a) for p_a, p_ab in
                      zip(self.cond_probs[pre_idx],
                          self.classified_probs[idx]) if p_a!=0]

            ans.append(self.words[p.index(max(p))])
        return ' '.join(ans)


def main():
    m, q = tuple(int(x) for x in input().split(' '))
    words = input().split(' ')
    reader = Reader(words)
    reader.read_input(input(), 'first_pos_probs')
    for i in range(m):
        reader.read_input(input(), 'cond_probs')
    for i in range(m):
        reader.read_input(input(), 'classified_probs')
    for i in range(q):
        reader.read_words(input().split(' ')[1:])






