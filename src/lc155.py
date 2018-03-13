class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minvalue = float('inf')
        

    def push(self, x):
        self.stack.append(x)
        if x < self.minvalue:
            self.minstack.append(x)
            self.minvalue = x

    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.minvalue:
            self.minstack.pop()
            if self.minstack:
                self.minvalue = self.minstack[-1]
            else:
                self.minvalue = float('inf')

    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.minvalue
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()