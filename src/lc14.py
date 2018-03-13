class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        strs.sort()
        ans = strs[0]
        if not ans:
            return ""
        
        for i in range(len(strs)):
            while ans and ans != strs[i][:len(ans)]:
                ans = ans[:-1]
            if not ans:
                return ""
        
        return ans
            