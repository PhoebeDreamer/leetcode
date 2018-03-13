import collections as c
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        dic = {'(':')', '[':']','{':'}'}
        q = []
        for v in s:
            if not q and v in dic.values():
                return False
            elif not q:
                q.append(v)
            elif v in dic:
                q.append(v)
            elif dic[q[-1]]==v:
                q.pop()
            elif dic[q[-1]]!=v:
                return False
        
        return not q