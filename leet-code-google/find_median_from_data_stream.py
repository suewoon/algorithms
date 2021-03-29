class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.current_length = 0
        self.list = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.list.append(num)
        self.current_length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        self.list = sorted(self.list)
        median_index = self.current_length // 2
        if (self.current_length % 2) == 0:
            return (self.list[median_index]+self.list[median_index-1])/float(2)
        else:
            return self.list[median_index]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()<Paste>
