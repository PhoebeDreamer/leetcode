class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # 重复的个数，加上去掉重复后，剩下的字符串个数
        # tmp = filter(None, B.split(A))
        # return len(tmp) + (len(B)-len("".join(tmp)))//len(A)
        
        # 但是如果b中没有a的完整重复，即b的长度小于a或2a，怎么判断呢？
        # 此时不可以用split
        # 且如果用a，b的数量来判断，无法准确判断，比如a = "abcde", b = "deab"
        # 但规律是如果b是a的重复，b的结尾+b的开头 in a 
        
        # 因此最终判断方法：如果重复，找到a的最大重复数times，b应该是a*times的一个substring
        # 逆向：一开始想要去掉b中重复的a，但是如果没有完整重复的a，很难找到；因此找到最大可能重复的a的组合，判断b是否在那个组合里
        
        times = -(-len(B)//len(A))
        # ceil
        for i in range(2):
            if B in A*(times+i):
                return times+i
        # i = 0时，适用于a = "abcde", b = "cdeabcdeabc"
        # i = 1时，适用于a = "abcde", b = "deabcdeab"
        
        return -1
                
                
                
            