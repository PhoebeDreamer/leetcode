class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        tmp = "1"
        while n-1:
            n-=1
            tmp = self.count(tmp)
        
        return tmp
            
    def count(self,s):
        ans = ""
        length = len(s)
        count = 1
        slow = 0
        fast = slow+1
        
        while fast<length:
            if s[slow] == s[fast]:
                count+=1
            else:
                ans= ans + str(count)+ s[slow]
                slow = fast 
                count = 1
            fast+=1
        
        if slow <= length-1:
            ans= ans + str(count)+ s[slow]

        return ans