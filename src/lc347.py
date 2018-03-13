class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        dic = collections.Counter(nums).most_common(k)
        ans = []
        
        for key, value in dic:
            ans.append(key)
        
        return ans