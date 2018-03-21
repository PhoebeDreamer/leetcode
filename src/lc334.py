class Solution1(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        tmp = float('inf')
        for i in range(len(nums)):
            if i==0:
                stack.append(nums[i])
            else: 
                if nums[i]>tmp:
                    return True
                if nums[i] in stack:
                    continue
                    
                if nums[i]<stack[-1]:
                    if len(stack)==2:
                        tmp = min(tmp, stack[-1])
                    while stack and nums[i]<=stack[-1]:
                        stack.pop()        
                stack.append(nums[i])

                if len(stack)>=3:
                    return True
            
        return False  
            
class Solution2(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1, n2 = float('inf'), float('inf')
        for n in nums:
            if n<=n1:
                n1 = n
            elif n<=n2:
                n2 = n
            else:
                return True
        return False
            