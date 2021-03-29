# https://leetcode.com/problems/maximal-square
class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n  = len(matrix), len(matrix[0])
        res = 0
        max_res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    res = 1
                    flag = True
                    #
                    # i, j 에서 갈 수 있는 최대 정사각형 길이
                    while i+res < m and j+res < n and flag:
                        for k in range(j, j+res+1):
                            if matrix[i+res][k] == "0":
                                flag = False # 정사각형이 안될 것 같으면 빠져나온다
                                break
                        for k in range(i, i+res+1):
                            if matrix[k][j+res] == "0":
                                flag = False
                                break
                        if (flag):
                            res+=1
                    max_res = max(max_res, res)

        return max_res*max_res
