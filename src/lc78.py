class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        sub = [[]]
        for n in nums:
            sub += [[n] + s for s in sub]
        
        return sub