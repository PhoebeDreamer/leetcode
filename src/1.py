class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        dic = {}
        for i, v in enumerate(nums):
            if v in dic:
                return [dic[v], i]
            else:
                dic[target-v] = i
        