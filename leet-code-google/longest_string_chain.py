class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda x: len(x))
        graph = {k:1 for k in words}
        res = 1

        for word in words:
            for i in range(len(word)):
                sub_str = word[:i]+word[i+1:]
                if sub_str in graph:
                    graph[word] = graph[sub_str] + 1
                    res = max(res, graph[word])

        #print(graph)
        return res
