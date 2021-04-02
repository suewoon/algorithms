class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])

        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        path = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(matrix, i, j, path):
            if path[i][j] != 0:
                return path[i][j]

            max_res = 1
            for next_x, next_y in [(i+dx[k], j+dy[k]) for k in range(4)]:
                if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] > matrix[i][j]:
                    path[i][j] = max(path[i][j], dfs(matrix, next_x, next_y, path))

            path[i][j] += 1
            return path[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(matrix, i, j, path))

        return res
