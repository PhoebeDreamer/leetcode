class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        count = 0
        ans = []
        for s in strs:
            tmp = ''.join(sorted(list(s)))
            if tmp not in res:
                res[tmp] = []
            res[tmp].append(s)
               
        return res.values()