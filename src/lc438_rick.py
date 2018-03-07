#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        idea: sliding-window + hashset
        由于这道题的sliding-window是fix-length的, 从而, 不需要双指针的双循环的较复杂控制.
        这道题教会了我: sliding-window的实现时, 能固定长度则固定长度, 这样会简单得多.
        """
        if len(s) < len(p):
            return []
        pcounter = Counter(p)
        scounter = Counter(s[:len(p)])
        ret = []
        s_end = len(p)
        while s_end <= len(s):
            if pcounter == scounter:
                ret.append(s_end-len(p))
            # remove oldest point in s window
            scounter[s[s_end - len(p)]] -= 1
            if scounter[s[s_end - len(p)]] == 0:
                del scounter[s[s_end - len(p)]]
            if s_end == len(s):
                break
            scounter[s[s_end]] += 1
            s_end += 1
        return ret

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
