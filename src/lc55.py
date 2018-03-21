class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        target = len(nums)-1
        dis = 0
        while i <= dis and i <= target:
            dis = max(dis, i+nums[i])
            if dis>=target:
                return True
            i+=1
        
        return False

class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        right = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i]>=right:
                right = i
        
        return right==0