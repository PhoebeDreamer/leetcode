# faster
class Solution1:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        tmp_sum = 0
        l = float('inf')
        
        for i in range(len(nums)):
            tmp_sum += nums[i]
            
            while slow<=i and tmp_sum>=s:
                l = min(l, i-slow+1)
                tmp_sum-=nums[slow]
                slow+=1
        
        return 0 if l>len(nums) else l
            

class Solution2:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = float('inf')
        for i in range(len(nums)):
            if i==0:
                tmp_sum = nums[0]
                fast = 0
            else:
                tmp_sum -= nums[i-1]

            while fast<len(nums)-1 and tmp_sum<s:
                fast+=1
                tmp_sum += nums[fast]               
            
            if tmp_sum>=s:
                l = min(l, fast-i+1)
            if l==1:
                return 1
        
        return 0 if l>len(nums) else l
            
            