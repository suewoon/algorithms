class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        temp = copy.copy(newInterval)
        while intervals:
            curr_interval = intervals[0]
            if curr_interval[1] < newInterval[0]:
                result.append(curr_interval)
            elif curr_interval[0] > newInterval[1]:
                break
            else:
                temp += curr_interval
                temp.sort()
            intervals = intervals[1:]
        result.append([temp[0], temp[-1]])
        #print(intervals)
        result+=intervals
        return result
            
        
