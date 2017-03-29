class SnailProblem(object):
    """
    snail climbs out of a well. he climbs up 2m/day if it's rainy 
    or 1m/day if it's clear. 
    Using discrete distribution library
    """
    def __init__(self, n, m):
        self.n = n #the well is n meter deep 
        self.m = m #the rainy season lasts for m days
        self.r = n-m
        assert(int==type(n) and int==type(m) and r>=0)
        self.p = 0.75

    def getProb(self):



testcase = int(input())
assert(int == type(testcase) and testcase <= 50 and 1 >= testcase)
for i in range(testcase):
    (n,m)  = tuple(input.split())
    snailProblem = SnailProblem(n,m)
    print(snailProblem.getProb)
    
#==============================================================================
# 
# import scipy.stats as ss
# 
# n = 15         # Number of total bets
# p = 18./38     # Probability of getting "red" at the roulette
# max_sbets = 4  # Maximum number of successful bets
# 
# hh = ss.binom(n, p)
# 
# total_p = 0
# for k in range(1, max_sbets + 1):  # DO NOT FORGET THAT THE LAST INDEX IS NOT USED
#     total_p += hh.pmf(k)
#==============================================================================
