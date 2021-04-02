class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLength = 0

        # odd length
        # i가 palindrome의 중심
        for i in range(len(s)):
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if resLength < len(s[l:r+1]):
                    res = s[l:r+1]
                    resLength = len(res)
                l-=1
                r+=1

        # even length
        # i, i+1이 palindrome의 중심
        for i in range(len(s)-1):
            l, r = i, i+1
            while 0<=l and r<len(s) and s[l] == s[r]:
                if resLength < len(s[l:r+1]):
                    res = s[l:r+1]
                    resLength = len(res)
                l-=1
                r+=1

        return res

