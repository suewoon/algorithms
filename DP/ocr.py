#!/usr/bin/env python3
import numpy as np 

class Reader(object):
    def __init__(self, words):
        self.words = words
        self.first_pos_probs = []
        self.cond_probs = []
        self.classified_probs = []

    def read_input(self, _input, param):
        _list = [float(x) for x in _input.split(' ')]
        if param == 'first_pos_probs':
            self.first_pos_probs.append(_list)
        elif param == 'cond_probs':
            self.cond_probs.append(_list)
        elif param == 'classified_probs':
            self.classified_probs.append(_list)

    def read_words(self, _input):
        _input = _input.split(' ')[1:]
        print('input', _input)
        ans = []
        for word in _input:
            if _input.index(word) == 0:
                p = [(p_ab*p_a) for p_a, p_ab in zip(self.first_pos_probs[0], self.classified_probs[0]) if p_a != 0]
            else:
                idx = self.words.index(word)
                pre_idx = self.words.index(ans[-1])
                p = [(p_ab*p_a) for p_a, p_ab in zip(self.cond_probs[pre_idx],
                                                     np.array(self.classified_probs)[:, idx]) if p_a != 0]
            print(word, p, p.index(max(p)))
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
        reader.read_words(input())


if __name__ == '__main__':
    main()






