class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 or not s2 or len(s1)>len(s2):
            return False
        
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2[0:len(s1)]) 
        if c1 == c2:
            return True
        
        i = 1
        while i <= len(s2)-len(s1):
            c2[s2[i-1]] -= 1
            if c2[s2[i-1]] == 0:
                del c2[s2[i-1]]
            
            c2[s2[i+len(s1)-1]]+=1
            
            if c1 == c2:
                return True
        
            i+=1
        
        return False