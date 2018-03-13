class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low = 0
        res = 1
        if len(s) == 0:
            return 0
        for high in range(len(s)):
            if s[high] in s[low:high]:
                if high - low > res:
                    res = high - low
                low = low + s[low:high].find(s[high]) + 1
        return max(res, high - low + 1)