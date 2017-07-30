#!/usr/bin/env python3
#################################################################################
################################## Algorithms ##################################
################################################################################

def attempt1(problem):
 
    # if it's empty array, return None
    if problem.numRow <= 0 or problem.numCol <= 0:
        return None

    # divide by median point of (0, problem.numCol)
    med = problem.numCol//2

    # define subproblem area 
    (subStartR, subNumR) = (0, problem.numRow)
    (subStartC1, subNumC1) = (0, med)
    (subStartC2, subNumC2) = (med + 1, problem.numCol - med -1)

    subprobs = []
    subprobs.append((subStartR, subStartC1, subNumR, subNumC1))
    subprobs.append((subStartR, subStartC2, subNumR, subNumC2))

    # get the all locations in dividing column 
    divider = crossProduct(range(problem.numRow), [med])

    # find the global maximum value in dividing column
    maxLoc = problem.getMaximum(divider)

    # find a neighbor in the same row which is greater than or equal to maxLoc
    neighbor = problem.getGreaterNeighbor(maxLoc)

    # found a 2D peak, return it 
    if neighbor == maxLoc :
        return maxLoc

    # otherwise, figure out which subproblem has the neighbor 
    # and then, recurse in that half

    sub = problem.getSubProblemHaving(subprobs, neighbor)
    result = attempt1(sub)
    return problem.getLocation(sub, result)


def crossProduct(list1, list2):
    '''
    returns all locations with x from list1 and y from list2
    '''
    return [(x, y) for x in list1 for y in list2]
