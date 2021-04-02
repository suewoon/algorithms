mport heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = [float('inf')]
        self.right_heap = [float('inf')]


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        top_left_value = self.left_heap[0]
        top_right_value = self.right_heap[0]

        if num < top_left_value*-1:
            heapq.heappush(self.left_heap, num*-1)
        else:
            heapq.heappush(self.right_heap, num)

        if len(self.right_heap) > len(self.left_heap) + 1:
            heapq.heappush(self.left_heap, heapq.heappop(self.right_heap)*-1)

        if len(self.left_heap) > len(self.right_heap):
            heapq.heappush(self.right_heap, heapq.heappop(self.left_heap)*-1)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left_heap) == len(self.right_heap):
            return (self.left_heap[0]*-1+self.right_heap[0])/float(2)
        else:
            return (self.right_heap[0])



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
