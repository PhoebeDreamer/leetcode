class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res+=1
            l, h = i-1, i+1
            # 奇数回文
            while l>=0 and h<len(s) and s[l]==s[h]:
                res+=1
                l-=1
                h+=1
            l, h = i, i+1
            while l>=0 and h<len(s) and s[l]==s[h]:
                res+=1
                l-=1
                h+=1
            # 偶数回文
        
        return res