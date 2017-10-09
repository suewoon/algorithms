#!/usr/local/bin python3
#  solution for: https://www.hackerrank.com/challenges/connected-cell-in-a-grid

def get_max_region(mat, n, m):
    '''
    return the number of cells in the largest region in the given matrix
    '''
    def get_neighbors(i, j):
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1),
                         (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]
        neighbors = list(filter(lambda x: x[0]>=0 and x[0]<n and x[1]>=0 and
                                x[1]<m, neighbors))
        return neighbors

    def dfs_visit(i, j, visited):
        for (x, y) in get_neighbors(i, j):
            if (x, y) not in visited and mat[x][y] == 1:
                visited.append((x,y))
                dfs_visit(x, y, visited)

        return visited

    visited_total = []
    visited_set = set()

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited_set and mat[i][j] == 1:
                visited = dfs_visit(i, j, [(i, j)])
                visited_total.append(len(visited))
                visited_set = visited_set.union(set(visited))
    
    return max(visited_total)

if __name__ == '__main__':
    n = int(input())
    mat = []
    m = int(input())
    mat.append(list(map(int, input().split())))
    print(get_max_region(mat))
