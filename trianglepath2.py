
class TriPathProblem(object):
    """
    Given the value of each step, choose the path where the summation of
    steps is the max
    """
    class Tripath(object):
        def __init__(self, row, pathVal):
            assert(int == type(row))
            self.pathVal = pathVal
            self.row = row
            self.cache1 = [[-1]*row for i in range(row)] #cache for optimalPath

    def __init__(self, row, pathVal):
        self.triPath = self.Tripath(row, pathVal)
        self.cache2 = self.triPath.cache1[:] #cache for countOptimalPath

    def optimalPath(self, x, y):
        if y == self.triPath.row - 1:
            return self.triPath.pathVal[y][x]

        if self.triPath.cache1[y][x] != -1:
            return self.triPath.cache1[y][x]
        ans = 0
        ans = self.triPath.pathVal[y][x] + max(self.optimalPath(x, y + 1), self.optimalPath(x + 1, y + 1))
        self.triPath.cache1[y][x] = ans
        return ans

    def countOptimalPath(self, x, y):
        if y == self.triPath.row - 1:
            return 1

        if self.cache2[y][x] != -1 :
            return self.cache2[y][x]

        ans = 0
        if self.optimalPath(x, y+1) >= self.optimalPath(x+1, y+1):
            ans += self.countOptimalPath(x,y+1)

        if self.optimalPath(x+1, y+1) >= self.optimalPath(x, y+1):
            ans += self.countOptimalPath(x+1, y+1)

        return ans


testcase = int(input())
assert (int == type(testcase) and testcase >= 1)
for i in range(testcase):
    row = int(input())
    pathVal=[]
    for j in range(row):
        pathVal.append([int(j) for j in input().split()])
    p = TriPathProblem(row,pathVal)
    print(p.countOptimalPath(0,0))
