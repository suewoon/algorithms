# https://leetcode.com/problems/two-sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        kv_map = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in kv_map.keys():
                # 저장해둔것 들중 짝이 있으면 리턴
                return [kv_map[complement], i]
            # 짝이 안맞으면 저장
            kv_map[nums[i]] = i
