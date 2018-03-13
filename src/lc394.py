class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        i, ans = self.decode(s, 0)
        return ans
    
    def decode(self, s, i):
        res = ""
        while i < len(s) and s[i]!=']':
            n = 0
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    n = n*10 + int(s[i])
                    i+=1
                
                i+=1 
                index, tmp = self.decode(s, i)
                i=index+1
                
                while n:
                    res+=tmp
                    n-=1       
            else:
                res+=s[i]
                i+=1
        
        return i, res
            


class Solution2(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [["", 0]]
        n = 0
        for i, v in enumerate(s):
            if v.isdigit():
                n = n*10 + int(v)
            elif v=='[':
                stack.append(["", n])
                n=0
            elif v==']':
                tmp, count = stack.pop()
                stack[-1][0] += tmp*count
            else:
                stack[-1][0]+=v
        
        return stack[0][0]
                
            