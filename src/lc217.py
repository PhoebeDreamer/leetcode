class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        tmp = set()
        for n in nums:
            if n not in tmp:
                tmp.add(n)
            else:
                return True
        
        return False