class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {j:0 for j in J}
        
        for s in S:
            if s in dic:
                dic[s] += 1
                
        return sum(dic.values())
        