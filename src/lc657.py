class Solution1(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h, v = 0, 0
        for m in moves:
            if m == 'U':
                v+=1
            if m=='D':
                v-=1
            if m=='L':
                h+=1
            if m=='R':
                h-=1
                
        return h==0 and v==0

class Solution2(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("L")  == moves.count("R") and moves.count("U") == moves.count("D")