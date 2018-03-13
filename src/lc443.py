class Solution:
    def compress(self, chars):
        if not chars:
            return 0
        
        slow = 0
        fast = 1
        while fast < len(chars):
            count = 1
            while fast<len(chars) and chars[fast] == chars[slow]:
                fast+=1
                count+=1
            
            if count>1:
                chars[:] = chars[:slow+1] + list(str(count)) + chars[fast:]
                slow += len(str(count)) + 1
                fast = slow +1
            else:
                fast+=1
                slow=fast-1
            
        return len(chars)