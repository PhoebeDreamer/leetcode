class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for n in t:
            if n not in dic:
                dic[n]=1
            else:
                dic[n]+=1
        
        for n in s:
            dic[n]-=1
        
        for n in dic:
            if dic[n] == 1:
                return n