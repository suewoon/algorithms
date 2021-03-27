# https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.memo = None
        self.makeMemo()
        

    def makeMemo(self):
        m = len(self.matrix)
        n = len(self.matrix[0])
        if m == 0 or n == 0: return
        self.memo = [[0 for j in range(n+1)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.memo[i][j+1] = self.memo[i][j] + self.matrix[i][j]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
    
        res = 0
        for i in range(row1, row2+1):
            res = res + self.memo[i][col2+1] - self.memo[i][col1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
