#!/usr/bin/env python3
import numpy as np 

class Reader(object):
    def __init__(self, words):
        self.words = words # of states
        self.initial_probs = []
        self.transition_probs = []
        self.emission_probs = []

    def read_input(self, _input, param):
        _list = [float(x) for x in _input.split(' ')]
        if param == 'initial_probs':
            self.initial_probs.append(_list)
        elif param == 'transition_probs':
            self.transition_probs.append(_list)
        elif param == 'emission_probs':
            self.emission_probs.append(_list)

    def read_words(self, _input):
        _input = _input.split(' ')[1:]
        self.emission_probs = np.array(self.emission_probs)
        self.transition_probs = np.array(self.transition_probs)
        self.initial_probs = np.array(self.initial_probs)
        
        
        T = len(_input) # observations
        N = len(self.words) # sates

        alpha = np.array([ [float('-inf') for _ in range(N)] for _ in range(T) ])#T(obs)*N(state) cache
        backpointers = np.array([ [-1 for _ in range(N)] for _ in range(T)])

        alpha[0, :] = self.initial_probs[0]*self.emission_probs[:,0]

        for t in range(1, T):
            for s1 in range(N):
                for s2 in range(N):
                    prob = alpha[t-1, s1]*self.transition_probs[s1, s2]*self.emission_probs[s2,t]
                    if prob > alpha[t, s2]:
                        alpha[t, s2] = prob
                        backpointers[t, s2] = s1
        words_seq = []
        words_seq.append(np.argmax(alpha[T-1, :]))
        for i in range(T-1, 0, -1):
            words_seq.append(backpointers[i, words_seq[-1]])

        ans = [self.words[i] for i in list(reversed(words_seq))]
        return ' '.join(ans)
    

def main():
    m, q = tuple(int(x) for x in input().split(' '))
    words = input().split(' ')
    reader = Reader(words)
    reader.read_input(input(), 'initial_probs')
    for i in range(m):
        reader.read_input(input(), 'transition_probs')
    for i in range(m):
        reader.read_input(input(), 'emission_probs')
    for i in range(q):
        reader.read_words(input())


if __name__ == '__main__':
    main()






