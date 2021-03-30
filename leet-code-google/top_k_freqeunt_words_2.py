# https://leetcode.com/problems/top-k-frequent-words/
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        frequency = Counter(words)
        sorted_freq = [(-value, key) for key, value in frequency.items()]
        heapq.heapify(sorted_freq)
        return [heapq.heappop(sorted_freq)[1] for _ in range(k)]
