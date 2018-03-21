class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        slow=0
        count=0
        tmp=1
        for i, n in enumerate(nums):
            tmp *= n
            while slow<=i and tmp>=k:
                tmp//=nums[slow]
                slow+=1
            
            count+=i-slow+1
            # important!!! 排列组合个数！！！
            
        return count
                