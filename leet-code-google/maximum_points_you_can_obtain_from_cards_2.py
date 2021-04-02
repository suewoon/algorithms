class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left_ptr = k-1
        left_sum = sum(cardPoints[:k])
        right_ptr = len(cardPoints)-1
        right_sum = 0

        max_res = left_sum
        while left_ptr >= 0:
            left_sum -= cardPoints[left_ptr]
            right_sum += cardPoints[right_ptr]
            max_res = max(max_res, left_sum+right_sum)
            right_ptr -= 1
            left_ptr -= 1

        return max_res

