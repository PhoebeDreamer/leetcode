class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or len(s) < len(p):
            return []
        
        ans = []
        c = collections.Counter(p)
        q = collections.Counter(s[:len(p)-1])
        s_start = 0
        
        while s_start < len(s)-len(p)+1:
            if s[s_start+len(p)-1] not in c.keys():
                s_start = s_start+len(p)
                if s_start < len(s)-len(p)+1:
                    q = collections.Counter(s[s_start:s_start+len(p)])
                else:
                    break
            else:
                 q[s[s_start+len(p)-1]]+=1
            
            if q == c:
                ans.append(s_start)
            
            q[s[s_start]]-=1
            if q[s[s_start]]==0:
                del q[s[s_start]]
            
            s_start+=1
        return ans
                