class SnakeGame(object):

    def __init__(self, width, height, food):
        self.r = height
        self.c = width
        self.index = 0
        self.food = food
       
        self.q = collections.deque()
        self.q.append((0,0))
        
        self.snake = set()
        self.snake.add((0,0))
                
    def move(self, direction):
        new_head = self.headmove(self.q[0], direction)
        new_head_r, new_head_c = new_head

        if new_head_r<0 or new_head_r>=self.r or new_head_c<0 or new_head_c>=self.c:
            print "touch boundary"
            return -1 
        
        if self.index<len(self.food) and list(new_head) == self.food[self.index]:
            # got food, tail doesn't move
            self.index+=1    
        else:
            self.snake.remove(self.q.pop())  
            
        if new_head in self.snake:
            # print "touch body"
            return -1
            
        self.q.appendleft(new_head)
        self.snake.add(new_head)
        return self.index
        
    def headmove(self, node, direction):
        i, j = node
        if direction == 'U':
            i-=1
        if direction == 'D':
            i+=1
        if direction == 'L':
            j-=1
        if direction =='R':
            j+=1
        return (i, j)

    
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)