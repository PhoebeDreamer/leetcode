class Solution1:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ans = []
        if not n or not k:
            return []   
        nums = [i for i in range(1,n+1)]
        self.helper(nums, k, [], 0)
        return self.ans
        
    def helper(self, nums, k, partial, cur):
        if len(partial) == k:
            self.ans.append(list(partial))
            return
        
        for i in range(cur, len(nums)):
            if nums[i] not in partial:
                partial.append(nums[i])
                self.helper(nums, k, partial, i+1)
                partial.pop()

class Solution2:
    def combine(self, n, k):
        return list(itertools.combinations(range(1,n+1), k))
            