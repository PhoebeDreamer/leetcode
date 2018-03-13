class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        if right<10:
            return [i for i in range(left, right+1)]
        
        for n in range(left, right+1):
            if n<10:
                ans.append(n)
            elif n%10:
                tmp = n
                flag = True
                while tmp:
                    t = tmp%10
                    tmp//=10
                    if not t or n%t:
                        flag = False
                if flag: ans.append(n)
        
        return ans
                    
                
                