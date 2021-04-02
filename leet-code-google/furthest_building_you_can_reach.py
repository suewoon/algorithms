# https://leetcode.com/problems/furthest-building-you-can-reach/
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        ladder_allocations = [] # min-heap
        for i in range(len(heights)-1):
            climb = heights[i+1]-heights[i]
            # skip
            if climb <= 0:
                continue
            # allocate ladder for this climb
            heapq.heappush(ladder_allocations, climb)
            # 있는 ladder를 아직 다 안썼다면 pass
            if len(ladder_allocations) <= ladders:
                continue
            # ladder를 다썼다면 brick과 바꿔줘야함
            bricks -= heapq.heappop(ladder_allocations)
            # bricks < 0이 되었다면 더이상 전진 할 수 없음
            if bricks < 0:
                return i
        return len(heights)-1
