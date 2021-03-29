# https://leetcode.com/problems/longest-palindromic-substring/
# time limit exceed
class Solution(object):
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return self.isPalindrome(s[1:-1])

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.isPalindrome(s[i:j]):
                    if len(res) < len(s[i:j]):
                        res = s[i:j]
        return res
