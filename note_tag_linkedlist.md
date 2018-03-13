# Node on Linked List

* linked list的连接和切断
    * 综合实例: 
        1. Split Linked List in Parts: lc[725](src/lc725.py)
        2. Odd Even Linked List: lc[328](src/lc328.py)
            + 善用dummy
        3. Remove Duplicates from Sorted List: lc[83](src/lc83.py)
        4. Remove Duplicates from Sorted List: lc[82](src/lc82.py)
        5. Remove Nth Node From End of List: lc[19](src/lc19.py)
            + 快慢指针 or dfs
        6. Partition List: lc[86](src/lc86.py)

*  Reverse Linked List(in k group)
    * 善用dummy，prev等
    * 综合实例：
        1. Reverse Linked List: lc[206](src/lc206.py) 
        2. Reverse Linked ListII: lc[92](src/lc92.py) 
        3. swap nodes(two): lc[24](src/lc24.py) 
        4. Reverse k group: lc[25](src/lc25.py)
        5. Palindrome Linked List: lc[234](src/lc234.py)
    * 模板
    ```python
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur
    ```

* Merge Sorted Lists
    * 需要注意两个list的长度不同，甚至可能出现一个list为空的情况
    * 综合实例：
        1. Merge Two Sorted Lists: lc[21](src/lc21.py)
        2. Merge K Sorted Lists: lc[23](src/lc23.py)
        3. Add Two Number

* List Cycle
    *  如果linked list存在cycle，那么快慢两个指针最终一定会相遇
    * 综合实例：
        1. Linked List Cycle：lc[141](src/lc141.py)
        2. Linked List CycleII: lc[142](src/lc142.py)
            + Floyd’s cycle detection algorith/Tortoise and Hare Algorithm

* Intersection of two linked lists
    * 相当于merge两个linked lists，规律就是肯定是在后半段merge，所以跳过两者的长度差
    * 综合实例：
        1. Intersection of Two Linked Lists：lc[160](src/lc160.py)
        2. Add Two Numbers: lc[2](src/lc2.py)