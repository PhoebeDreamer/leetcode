class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :idea: 从中间开始分，冗余的一边比另一边多一些元素
        """
        if not nums:
            return None
        high = len(nums)
        low = 1
        mid = (high+low)//2
        
        while mid <= len(nums):
            count, flag = 0, 0
            for n in nums:
                if n == mid:
                    flag += 1
                    if flag >= 2:
                        return mid
                                     
                if n < mid:
                    count+=1
            
            if count < mid:
                low = mid
            else:
                high = mid
            
            mid = (high+low)//2
            
        return mid
        