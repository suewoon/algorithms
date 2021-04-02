#https://leetcode.com/problems/longest-palindromic-substring/
# timelimit exceeded
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = ""
        resLength = 0

        # 길이 1 인 substring
        for i in range(len(s)):
            self.memo[i][i] = True
            resLength = 1
            res = s[i:i+1]

        # 길이 2인 substring
        for i in range(len(s)):
            if i+1 < len(s) and (s[i] == s[i+1]):
                self.memo[i][i+1] = True
                res = s[i:i+2]
                resLength = 2

        for i in range(len(s)-1,-1,-1):
            for j in range(2, len(s)-i):# 길이
                #print(s[i:i+j+1], s[i+1:i+j], self.memo[i+1][i+j-1], i, j+i)
                self.memo[i][i+j] = self.memo[i+1][i+j-1] and s[i] == s[i+j]
                if self.memo[i][i+j] and resLength < len(s[i:i+j+1]):
                    res = s[i:i+j+1]
                    resLength = len(res)

        return res
