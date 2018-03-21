import collections as c
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dummyhead = Node()
        self.dummytail = Node()
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead
        self.mem = {}
        self.capacity = capacity
        # print("init success!")

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mem:
            # print("no found")
            return -1

        node = self.mem[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.append(node)        
        # print("get", node.key, node.val)
        return node.val

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.mem:
            if len(self.mem) >= self.capacity:
                tmp = self.dummyhead.next
                # print("pop", tmp.key, tmp.val)
                del self.mem[tmp.key]
                self.dummyhead.next = tmp.next
                tmp.next.prev = self.dummyhead

            next_node = Node(key, value)
            self.mem[key] = next_node
            # print("add", next_node.key, next_node.val)
            self.append(next_node)

        else:
            node = self.mem[key]
            node.val = value                  
            node.prev.next = node.next
            node.next.prev = node.prev
            self.append(node)

            
    def append(self, node):
        tmp = self.dummytail.prev
        tmp.next = node
        node.prev = tmp
        self.dummytail.prev = node
        node.next = self.dummytail



            
            
        

        
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)