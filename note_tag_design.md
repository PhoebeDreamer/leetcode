### Note on Design
* 思路：用现有的数据结构来实现一个类    

* 设计数据结构
    * 使用double linked list和hash
        1. LRU Cache [lc146](src/lc146.py)
            * get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
            * put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
            ```
            LRUCache cache = new LRUCache( 2 /* capacity */ );

            cache.put(1, 1);
            cache.put(2, 2);
            cache.get(1);       // returns 1
            cache.put(3, 3);    // evicts key 2
            cache.get(2);       // returns -1 (not found)
            cache.put(4, 4);    // evicts key 1
            cache.get(1);       // returns -1 (not found)
            cache.get(3);       // returns 3
            cache.get(4);       // returns 4
            ```
            * 解法：
                + 数据结构：一个double-linked list类，包含pre，next，key，value
                + init：head，tail，capacity，mem{key:node}
                + get()：如果key不在mem中，返回-1；否则返回mem[key].val，swap(node,node.next)
                + put(): 
                
                    ```mermaid
                    graph TB
                        A{if key in mem?}
                        A -->|NO| B{capacity enough?} 
                        A -->|YES| C[update node.val]
                        B -->|Yes| D[append new node]
                        B -->|NO| E[pop the eldest one]
                        C --> F[swap node and node.next]
                        E --> D
                    ``` 
        
        2. LFU Cache [lc460](src/lc460.py)
            * get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
            * put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
            ```
            LFUCache cache = new LFUCache( 2 /* capacity */ );

            cache.put(1, 1);
            cache.put(2, 2);
            cache.get(1);       // returns 1
            cache.put(3, 3);    // evicts key 2
            cache.get(2);       // returns -1 (not found)
            cache.get(3);       // returns 3.
            cache.put(4, 4);    // evicts key 1.
            cache.get(1);       // returns -1 (not found)
            cache.get(3);       // returns 3
            cache.get(4);       // returns 4
            ```
            * 解法：
                + 数据结构：一个double-linked list类，包含pre，next，key，value，freq
                + init：head，tail，capacity，mem{key:node}，rank{freq:node}
                + get()：如果key不在mem中，返回-1；否则返回mem[key].refresh node
                + put()
                ```mermaid
                    graph TB
                        A{if key in mem?}
                        A -->|NO| B{capacity enough?} 
                        A -->|YES| C[update node.val]
                        C --> D[find the place to insert node, and update rank and mem]
                        D --> B
                        B -->|Yes| F[append new node, and update rank and mem]
                        B -->|NO| E[pop the eldest one, and update rank and mem]
                        E --> F
                ``` 
            * 难点：每一步都要记得维护mem和rank，如果插入node，跟rank关系很大。比如如果node的freq+1，那么需要看freq是否在rank，如果不在，node就会放到head前面；如果在，需要看rank[freq]是否是node：如果不是node，那么直接放到rank[freq]前面就好了;如果是node，就要看node.prev.freq是否是freq：如果是，则update rank[freq]，如果不是，则删掉rank[freq]
    