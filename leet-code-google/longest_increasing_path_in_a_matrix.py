# time limit exceeded
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        max_res = 1

        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        from collections import deque

        for i in range(m):
            for j in range(n):

                queue = deque([(i,j)])
                visited = []
                path = [[0 for _ in range(n)] for _ in range(m)]
                path[i][j] = 1

                while queue:
                    curr_x, curr_y = queue.popleft()
                    for next_x, next_y in [(curr_x+dx[k], curr_y+dy[k]) for k in range(4)]:
                        if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] > matrix[curr_x][curr_y]:
                            queue.append((next_x, next_y))
                            path[next_x][next_y] =  path[curr_x][curr_y] + 1

                #print('path', path)
                max_res = max(max_res, max(map(max, path)))

        return max_res
