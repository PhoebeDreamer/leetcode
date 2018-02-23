class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        digits = list(map(int, digits))
        self.ans = []
        self.max = len(digits)
        self.dic = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        self.helper(digits, 0, [])
        
        return self.ans
        
    def helper(self, digits, cur,  partial):
        if len(partial) == self.max:
            self.ans.append(''.join(partial))
        else:
            # for i in range(cur, self.max):
            for t in self.dic[int(digits[cur])]:
                # print(digits[i])
                partial.append(t)
                self.helper(digits, cur+1, partial)
                partial.pop()