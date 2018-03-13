class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 双向指针查询元音，找到就交换，因此example2交换了两次，但是第一次交换的字符相同
        alpha = {"a","e","o","i","u","A","E","O","I","U"}
        
        i = 0
        j = len(s) - 1
        s = list(s)
        
        while i < j:
            while i < j and s[i] not in alpha:
                i += 1
            while i < j and s[j] not in alpha:
                j -= 1
                
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
        return "".join(s)
            