class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if len(nums)<=1:
            return len(nums)
        
        index = 0
        for i in range(length):
            if nums[index]!=nums[i]:
                index+=1
                nums[index]=nums[i]
        
        return index+1
    

                
                    