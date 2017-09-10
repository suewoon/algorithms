#!/usr/bin/env python3
################################################################################
########################### Peak Problems D2 ###### ############################
################################################################################

class PeakProblem(object):
    def __init__(self, array, bounds):
        (startRow, startCol, numRow, numCol) = bounds

        self.array = array
        self.bounds = bounds 
        self.startRow = startRow
        self.startCol = startCol
        self.numRow = numRow
        self.numCol = numCol 

    def getMaximum(self, divider):
        '''
        return the location of which value is global maximum in divider column
        '''
        maxLoc  = None
        for loc in divider:
            if maxLoc is None or self.get(maxLoc) < self.get(loc):
                maxLoc = loc
        return maxLoc

    def get(self, location):
        '''
        return the value of a location
        '''
        (r, c) = location
        if not (0 <= r and r < self.numRow):
            return 0
        if not (0 <= c and c < self.numCol):
            return 0
        return self.array[self.startRow+r][self.startCol+c]

    def getGreaterNeighbor(self, location):
        '''
        
        '''
        (r, c) = location
        greatest_loc = location

        if r-1 >= 0 and self.get((r-1,c)) > self.get(greatest_loc):
            greatest_loc = (r-1,c)
        if c-1 >=0 and self.get((r,c-1)) > self.get(greatest_loc):
            greatest_loc = (r, c-1)
        if r+1 < self.numRow and self.get((r+1,c)) > self.get(greatest_loc):
            greatest_loc = (r+1,c)
        if c+1 < self.numCol and self.get((r,c+1)) > self.get(greatest_loc):
            greatest_loc = (r,c+1)

        return greatest_loc

    def getSubProblem(self, bounds):
        (sRow, sCol, nRow, nCol) = bounds
        newBounds = (self.startRow + sRow, self.startRow + sCol, nRow, nCol)
        return PeakProblem(self.array, newBounds)
    
    def getSubProblemHaving(self, boundList, location):
        (row, col) = location
        for (sRow, sCol, nRow, nCol) in boundList:
            if sRow <= row and row < sRow + nRow and sCol <= col and col < sCol + nCol:
                return self.getSubProblem((sRow, sCol, nRow, nCol))


    def getLocation(self, problem, location):
        (row, col) = location
        newRow = row + problem.startRow - self.startRow
        newCol = col + problem.startCol - self.startCol
        return (newRow, newCol)

    def isPeak(self, location):
        return (self.getGreaterNeighbor(location) == location)





