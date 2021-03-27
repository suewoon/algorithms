# https://leetcode.com/problems/decode-string/
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub_str = []
        temp_numerics = []
        numerics = []
        result = ""
        for char in s:
            if char == "[": # opening bracket
                sub_str.append([])
                numerics.append(int(''.join(temp_numerics)))
                temp_numerics = []
            elif char == "]": # closing bracket
                repeated_str = sub_str.pop()
                repeated_num = numerics.pop()
                if len(sub_str) > 0 and isinstance(sub_str[-1], list):
                    sub_str[-1] += repeated_num * repeated_str
                    merge = ''.join(sub_str[-1])
                    continue
                sub_str.append(''.join(repeated_num * repeated_str))
                
            elif char.isalpha():
                if len(sub_str) > 0 and isinstance(sub_str[-1], list):
                    sub_str[-1].append(char)
                    continue
                sub_str.append(char)  
            else:
                temp_numerics.append(char)
        return ''.join(sub_str)
