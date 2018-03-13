# from 光头哥
def longestSubstring1(self, s, k):
    for c in set(s):
        if s.count(c) < k:
            return max(self.longestSubstring(t, k) for t in s.split(c))
    return len(s)

# 自己写的
class Solution2(object):
    def longestSubstring(self, s, k):
        if not s:
            return 0
        if len(s)<k:
            return 0
        
        counter = collections.Counter(s)
        out = set()
        for v in counter:
            if counter[v] < k:
                out.add(v)
       
        # all freq<k
        if len(out)==len(counter):
            return 0
        # all freq>=k
        if not out:
            return len(s)
        
        # some freq<k
        index = 0
        tmp = ""
        # find the index of latest occurence of out, and divide
        for o in out:
            if index<s.rfind(o):
                index = s.rfind(o)
                tmp = o
        # continue the right rest part
        right = self.longestSubstring(s[index+1:],k)
        # filter duplicates and continue the left rest part
        while index>=0 and s[index]==tmp:
            index-=1
        left = self.longestSubstring(s[:index+1],k)
        
        return max(left, right)        
    

                