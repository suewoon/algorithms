# https://leetcode.com/problems/maximal-square/
class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n  = len(matrix), len(matrix[0])
        # (i, j) 가 정사각형에서 3사분면 위치
        # 구하고자 하는것이 면적, 즉 길이 이므로 정사각형에서3사분면을 기준으로
        # dynamic programming 수식 작성을 해야한다.
        minSquareMap = [[0 for i in range(n+1)] for j in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    minSquareMap[i][j] = min(minSquareMap[i][j-1], minSquareMap[i-1][j], minSquareMap[i-1][j-1])+1
                    res = max(res,minSquareMap[i][j])
        print(minSquareMap)
        return res*res
