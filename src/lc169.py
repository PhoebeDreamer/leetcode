class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        major = nums[0]
        for i in range(1,len(nums)):
            if not count:
                count+=1
                major = nums[i]
            elif major==nums[i]:
                count+=1
            else:
                count-=1
        
        return major