# timelimit exceeded
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        max_res = 0
        length = len(cardPoints)

        if k == length:
            return sum(cardPoints)

        memo = [[0 for i in range(length+1)] for i in range(length)]
        for i in range(length):
            for j in range(i, length+1):
                memo[i][j] = sum(cardPoints[i:j])

        #print(memo)

        for i in range(k//2+1):
            #print(i, length-k+i, memo[0][i], memo[length-k+i][length])
            max_res = max(max_res, memo[0][i]+memo[length-k+i][length])
            if i == 0:
                #print(k-i, memo[0][k-i])
                max_res = max(max_res, memo[0][k-i])
            else:
                max_res = max(max_res, memo[0][k-i]+memo[length-i][length])
                #print(k-i, length-i, memo[0][k-i], memo[length-i][length])
        return max_res
