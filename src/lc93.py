class Solution1:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []
        self.length = len(s)
        self.helper(s, 0, [])
        return self.ans
    
    def helper(self, s, cur, partial):
        if len(partial) == 4 and cur == self.length:
            tmp = ""
            for i in partial:
                tmp += i+"."      
            self.ans.append(tmp[:-1])
        elif len(partial)<4:
            tmp = ""
            for i in range(cur, cur+3):
                if i <= self.length-1:
                    if int(s[i])==0 and not tmp:
                        tmp = s[i]
                        partial.append(tmp)
                        self.helper(s, i+1, partial)
                        partial.pop()
                        break
                    elif int(tmp+s[i]) in range(1,256):
                        tmp+=s[i]
                        partial.append(tmp)
                        self.helper(s, i+1, partial)
                        partial.pop()

#revised version
class Solution2:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []
        self.helper(s, 0, "", 0)
        return self.ans
    
    def helper(self, ip, cur, partial, count):
        if len(partial) > 4: 
            return
        if len(partial) == 4 and cur < len(ip):
            return
        if len(partial) == 4 and cur == len(ip):
            self.ans.append(partial)
        
        tmp = ""
        for i in range(cur,cur+3):
            if i+1>len(ip):
                break
            tmp+=ip[i]
            if int(tmp) >=256:
                break
            if tmp.startwith("0") and len(tmp) > 1:
                break 
    
            if count == 3:
                self.helper(ip, i+1, partial+tmp, count+1)
            else:
                self.helper(ip, i+1, partial+tmp+'.', count+1)
        