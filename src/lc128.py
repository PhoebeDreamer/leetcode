class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cp = set(nums)
        ans = 1
        
        for n in cp:
            if n-1 not in cp:
                tmp = n+1
                while tmp in cp:
                    tmp += 1
                ans = max(ans, tmp-n)
        
        return ans        