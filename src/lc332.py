import collections as c
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return tickets
        self.dic = c.defaultdict(list)
        for frm, to in sorted(tickets)[::-1]
            self.dic[frm].append(to)
        
        self.route = []
        
        # print(self.dic)
        self.visit("JFK")
        return self.route[::-1]
    
    def visit(self, city):
        while self.dic[city]:
            self.visit(self.dic[city].pop())
        self.route.append(city)
            
            
            
            
            
            