class Node():
    def __init__(self, key=None, val=None, freq=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = None
        self.prev = None

class LFUCache:

    def __init__(self, capacity):
        self.dummyhead = Node()
        self.dummytail = Node()
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummytail
        self.capacity = capacity
        self.rank = {0:self.dummyhead}
        self.lib = {}
        
    def get(self, key):
        if key not in self.lib:
            return -1
        node = self.lib[key]
        self.refresh(node)
        return node.val
        
    def put(self, key, value):
        if not self.capacity:
            return 
        
        if key in self.lib:
            node = self.lib[key]
            node.val = value
            if self.rank[node.freq].key == node.key:
                self.rank[node.freq] = node
            self.refresh(node)
            return
        
        if len(self.lib) >= self.capacity:
            self.pop_first()
        self.add(key, value)

    def add(self, key, value):
        node = Node(key, value, 1)
        self.lib[key] = node
        
        frequence = 1
        if frequence in self.rank:
            prev_node = self.rank[frequence]
        else:
            prev_node = self.dummyhead
        
        self.rank[frequence] = node
        node.next = prev_node.next
        prev_node.next.prev = node
        node.prev = prev_node
        prev_node.next = node       
    
    def pop_first(self):
        tmp = self.dummyhead.next
        if self.rank[tmp.freq].key == tmp.key:
            del self.rank[tmp.freq]
        del self.lib[tmp.key]
        self.dummyhead.next = tmp.next
        tmp.next.prev = self.dummyhead
  
    def refresh(self, node):
        frequence = node.freq + 1       
        if frequence in self.rank:
            prev_node = self.rank[frequence]
            if self.rank[frequence-1].key == node.key:
                if node.prev.freq == frequence-1:
                    self.rank[frequence-1] = node.prev
                else:
                    del self.rank[frequence-1]
        else:
            if self.rank[frequence-1].key != node.key:
                prev_node = self.rank[frequence-1]
            else:
                prev_node = node.prev
                if node.prev.freq == frequence-1:
                    self.rank[frequence-1] = node.prev
                else:
                    del self.rank[frequence-1]
        self.rank[frequence] = node
        node.freq = frequence

        node.next.prev = node.prev
        node.prev.next = node.next

        node.next = prev_node.next
        prev_node.next.prev = node
        node.prev = prev_node
        prev_node.next = node







# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)