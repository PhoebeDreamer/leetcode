class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        tmp = {i:0 for i in range(1,length+1)}
        for n in nums:
            if n in tmp:
                tmp[n]+=1

        return [i for i in tmp if tmp[i] == 2] + [i for i in tmp if tmp[i] == 0]
    