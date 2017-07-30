#!/usr/bin/env python3
################################################################################
########################### D1 Peak Problems ###################################
################################################################################


class PeakProblem(object):
    def __init__(self):
        pass

    def median(self, seq):
        return len(seq)//2

    def peak_find(self, seq):
        print(seq)
        if len(seq) == 1:
            print(seq[0])
            return seq[0]
        med = self.median(seq)
        if seq[med-1] > seq[med] and (med-1) > -1:
            self.peak_find(seq[:med])
        elif seq[med+1] > seq[med] and (med+1) < len(seq) :
            self.peak_find(seq[med+1:])


def main():
    problem = PeakProblem()
    problem.peak_find([1, 3, 4, 3, 5, 1, 3])

if __name__ == '__main__':
    main()
