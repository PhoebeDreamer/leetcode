class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ''.join(s.split(" "))

        stack = []
        i = 0
        o = '+'
        while i < len(s):
            n=0
            while i<len(s) and s[i].isdigit():
                n = n*10 + int(s[i])
                i+=1
            
            if o=='+':
                stack.append(n)
            elif o == '-':
                stack.append(-n)
            elif o=='*':
                stack.append(stack.pop()*n)
            elif o=='/':
                tmp = stack.pop()
                if tmp<0:
                    stack.append(-(-tmp//n))
                else:
                    stack.append(tmp//n)
            
            if i < len(s):
                o = s[i]
            i+=1
        
        return 1 if not stack else sum(stack)
                
            
                
                
                
            
        