# phoebe leetcode
This is my leetcode practice book.

### lc[121](src/lc121.py) DP 

### [lc241](src/lc241.py) TODO tut'ed
idea: Divide and Conquer 

### [lc395](src/lc395.py) 
idea: Longest Substring with At Least K Repeating Characters， dfs, divide and conqure, 一开始想的是滑动窗口，但没有办法做出来，因为并没有固定的字符串去匹配，只有频率k。因此要找到freq<k的元素，然后以该元素为节点，divide，再分段conqure，直到找到符合要求的slice。

### [lc437](src/lc437.py) TODO tutored
idea: 

### [lc377](src/lc377.py) DP
idea: 

### [lc438](src/lc438_rick.py)
idea: hash table, sliding-window, Counter，滑动窗口。使用Counter时的技巧是，为了避免出现超时的情况，不应该对每一个窗口进行一次Counter操作，而是处理掉上一个窗口的第一个元素，如果处理后，Counter中该元素个数为0，则del。然后窗口往后移动一步，对最新的元素进行操作。

### [lc567](src/lc567.py)
idea: 待修改， Two Pointers， Sliding window， 类似438

### [lc617](src/lc617.py)
idea: Merge Two Binary Trees, Tree, preorder

### [lc226](src/lc226.py) 
idea: Tree, recursion, invert Binary Tree, Google homebrew

### [lc563](src/lc563.py)
idea: Tree，累加各层的绝对差，即左边的和减掉右边的和

### [lc114](src/lc114.py)
idea: Tree, DFS, Flatten Binary Tree, bottom to top，从下至上，遍历左边，再遍历右边，把左分支的最右边接到右分支上

### [lc526](src/lc526.py)
idea: Backtracking, 回溯，解题关键在于要从反方向进行筛选，否则会超时。

### [lc130](src/lc130.py)
idea: DFS, BFS, Union Find，题目表述不清楚系列，只要国土有在边界上，则不需要由‘O’变成'X‘,而是把'O'替换成"*"。最后再循环一次，"*" 替换为'O','O'的替换为'X'. 但是这样可能为出现重复访问，超时的情况，因此需要减少重复次数：找到边界国土时，进行四周visit时，要确保下一个值再往前后走时，不会再走到边界上，因此i>2或i<length-2

### [lc207](src/lc207.py)
idea: 选课系统，Course ScheduleI，DFS, Graph，Topological Sort，建立依赖地图和队列q，从被依赖度为0的node支点开始走，如果graph[node]中的支点的被依赖度也为0时，将该支点append进q，直至走完q中所有的支点。

### [lc210](src/lc210.py)
idea: 选课系统，Course ScheduleII，DFS，Graph，Topological Sort，类似lc207

### [lc630](src/lc630.py) GREEDYs
idea: 选课系统，Course ScheduleIII，greedy

### [lc332](src/lc332.py)
idea: DFS, Graph. Reconstrcut Itinerary, 飞行路线设计。先建立起一个map(from,to)，依次pop出map[from]，避免又回头走，导致circl存在。因为要按照lexical排，所以map[list]本身append进去时就有顺序，pop出去的应该是小的，但只有当一条路线走完时，才会append进去路线，因此得到的path是反的，最终的ans还要完全倒过来。此处虽然也是一个backtracking问题，但是是每一步都有限定范围，且只要visit过，都不会重复再走的问题。此题和选课问题不属于同一问题。 

### [lc22](src/lc22.py)
idea: backtracking，随机组合的顺序有限定，left和right的数量作比较

### [lc17](src/lc17.py) 
idea: backtracking，模板题，电话按键题，组合的范围有限定

### [lc538](src/lc538.py) 
idea: 二分查找树转为更大树，逆中序遍历，逐个改变节点值

### [lc78](src/lc78.py) 
idea: iteratively或backtracking；迭代：创造res，循环遍；回溯，模板套用

### [lc79](src/lc79.py) 
idea: backtracking + DFS, 遍历二维数组并标记路轨，寻找合适的轨迹

### [lc695](src/lc695.py)
idea: Array, DFS, Max Area of Island, 类似lc200，遍历四周为1的，然后area进行pk

### [lc200](src/lc200.py) 
idea: DFS，找到其中一个island（为1），遍历二维数组将其整个面积标记为0，然后寻找下一个island（1）（计数），最终二维数组整个为0 

### [lc733](src/lc733.py) 
idea: DFS，lc200相似解法，将目标坐标周围值全部替换为target，如果坐标合理且坐标值为1

### [lc93](src/lc93.py) 
idea: Backtracking，限定条件为长度，大小，字符串(>1)开头不可为0
总结：如果用数组，则要append，pop；如果用string，直接在helper函数里partial+new

### [lc103](src/lc103.py)
idea: BFS，deque, 把所有的放入list里面，但是需要加入level变量，倒叙偶数行

### [lc404](src/lc404.py)
idea: BFS，deque, 找到最左边的叶子的和

### [lc389](src/lc389.py)
idea: HashTable, 哈希表

### [lc771](src/lc771.py)
idea: Hash Table

### [lc215](src/lc215.py)
idea1: Binary Search, 分治法, 复杂的地方在于怎么处理重复的情况，因此不仅要有left，right，还要有equal
idea2: heap
### [lc77](src/lc77.py)
idea: Backtracking/combinations
* itertools自带combinations功能(combinations(list, k)),顺序无关
* permutations，顺序相关
* combinations_with_replacement，和combinationsl类似，但它生成的组合包含自身元素

### [lc46](src/lc46.py)
idea: Backtracking/Permutations

### [lc216](src/lc216.py)
idea: Backtracking
* trick1: k与n的个数存在一定的关系，求和公式，可以由此判断是否存在答案
* trick2：在helper中判断是否可以放入ans中时，加上一个return，可以减少运行时间

### [lc40](src/lc40.py)
idea: Backtracking，回溯，在数组中找到加和为target的组合，可以重复

### [lc39](src/lc39.py)
idea: Backtracking, 回溯

### [lc124](src/lc124.py) Important!!!
idea: DFS
* 如果是判断path，则需要比较left+right+root.val和max
* 但是此时的left，right都需要和0比较一下，存在传上来的值<0的情况
* 如果要往上传，则left，right只能选一个，需要比较left，right 

### [lc543](src/lc543.py) important!!!
idea: Tree, DFS, 找到最长路径，不需要穿过root，需要helper返回两个参数，一个是node左右最长的路径，一个是当前已记录的最大路径

### [lc687](src/lc687.py)
idea: DFS, Tree, 类似lc543，lc124.如果root.val与root.left.val相同，则left+1，否则left置为0，同理root.right。往上返回的是root的一边，left与right pk，且max要于left+right pk。

### [lc606](src/lc606.py)
idea: String，Tree

### [lc257](src/lc257.py)
idea: Tree, DFS，Backtracking，每次有分叉，就多了一条路径，本质是回溯

### [lc108](src/lc108.py)
idea: DFS, Binary Search，找到中间值做root，然后迭代，继续往下分

### [lc129](src/lc129.py)
idea: DFS, 类似lc257

### [lc94](src/lc94.py)
idea: inorder, dfs, stack，中序遍历，如何用iteratively实现

### [lc501](src/lc501.py)
idea：Tree, dfs, stcak, find the most frequent occured element in BST,

### [lc98](src/lc98.py)
idea1：DFS, Tree, top to bottom, 从上至下，考虑双边情况，树的左分支有一个ceiling，树的右分支有一个floor
idea2: BFS， Tree，bottom to top, 从下至上，采用while方法，遍历左边，再分支遍历右边，pre为stack的上一次pop出来的值，当前cur永远大于上一个pre的值（包含了root.val > root.left.val和root.val < root.right.val）

### [lc230](src/lc230.py)
idea：BST, Tree, find the k smallest element in BST, 利用BST的性质，root.left<root, root.right>root.

### [lc669](src/lc669.py) important!!!
idea: DFS, Tree，node如果小于min，则返回node.right;node如果大于max，则返回node.left；同时对】node.left和node.right进行递归

### [lc547](src/lc547.py) important!!!!!!!!!
idea: DFS, path标记，找到朋友圈个数，突破点在如果是两个独立的朋友圈a、b，则a绝不会出现在b所在的行或列上，即如果a出现在b所在行上，两者一定属于同一个朋友圈。
* 因为一开始只关注了怎么标记原二维数组，所以越写越乱 눈_눈

### [lc112](src/lc112.py)
idea: DFS, Tree. 判断是否存在一条路径从root出发直到最子叶，和为target。逆向思维，往下递归时，target减去已经走过的node.val，判断当为最子叶（not root.left and not root.right)时，target是否和node.val相同。

### [lc113](src/lc113.py)
idea: DFS, Tree. Path SumII，同理lc112，只是函数多加了一个partial参数，因为要记录走过的路径。

### [lc235](src/lc235.py)
idea: DFS, Tree. find the Lowest Common Ancestor of two given nodes in BST. 利用BST的性质，根大于左子树，小于右子树。如果node p、q的值都大于node.val，则返回node.right，如果p、q的值都小于node.val，则返回node.left,如果node.val介于p、q中间，则返回node。

### [lc236](src/lc236.py)
idea: DFS, Tree. find the Lowst Common Ancestor of two given nodes in Binary Tree. 在二叉树中左右寻找支点p、q，left是左边寻找的结果，right是右边寻找的结果。如果root is p or q，则返回root。只有三种可能的结果：1.left和right都返回了结果；2.p是q的子节点；3.q是p的子节点。如果left和right都返回了结果，则返回root，否则如果只有一侧返回结果，只需要返回该结果即可。

### [lc116](src/lc116.py)
idea: DFS, Tree, populating next right pointers in each node I, 前置条件，平衡树，依次把左右连接起来，并且如果当前root有next的话，要把root.right指向root.next.left。

### [lc117](src/lc117.py)
idea: BFS, DFS，Tree, populating next right pointers in each node II, 前置条件，非平衡树
* 解法1：BFS， 三个指针，root指向parent，tail指向child，dummy有两个作用：1.用来存储已经生成的child的next关系，2.是一个空指针。最难理解的点在于，如果parent层已经走完，root指向空时，update指针时，将已经生成的child层的关系assign给root，即root=dummy.next，但是child层要置空，指向空，因此tail=dummy。
* 解法2：DFS，但可能不是constant space，暂时放弃

### [lc199](src/lc199.py)
idea: BFS, DFS，Tree，Binary Tree Right Side View,找到二叉树每层最右边的值
* 解法1：BFS，deque(level, node)，ans:list[list]，把每一层都存到ans，问题是怎么放，因为list必须有index，一个特别的方法，当len(ans)<level时，就在最开头插入一个list(ans.insert(0,[]))，放的时候倒着放(ans[-level].append(node))
* 解法2：DFS，从右边开始迭代，每当len(ans)==curdepth时，ans.append(node.val)
* 解法3：BFS, deque(node)，对每一层都有一个循环(for i in range(len(q)))，result接住第一个node，然后把剩下的都pop出去.

### [lc104](src/lc104.py)
idea: DFS, Tree, Maximum Depth of Binary Tree, 左右分支深度pk，返回pk结果+1

### [lc110](src/lc110.py)
idea: DFS, Tree, Balanced Binary Tree, lc104的进阶版，除了要得出每层的深度，还要判断是否左右分支的深度是否大于1.

### [lc100](src/lc100.py)
idea: DFS, Tree, Same Tree, 判断两个树是否完全一样，注意判断两个树是否状态(即空或不空)，直接用p is q

### [lc101](src/lc101.py) 
idea: Tree, DFS, BFS, 判断树是否对称，lc100的进阶版
* dfs:由basic case往下推，1个node只需要判断left,right是否相同；两个node需要判断left.left与right.right，left.right与right.left;更多node的时候，最左边，最右边（依次往内）判断是否对称【边际到中央】
* bfs：利用stack，push进去left，right，情况较为复杂

### [lc204](src/lc204.py)
idea: Math, Hash Table, Count Primes, 质数相关的题都可以用的解法，从i*i开始走，步伐为i

### [lc172](src/lc172.py)
idea: Math, Factorial Trailing Zeros, 找到n！尾巴0的个数。只要存在5，就会有一个0，trick是怎么解决25的问题。只需要让n//=5, count+=n即可。

### [lc155](src/lc155.py)
idea: stack, design, Min Stack, 具有pop，push，pop，getMin的功能，如果要在constant time里获得，最主要的问题就是pop的时候怎么处理getMin函数会被影响。因此有两个list，stack和minstack，以及minvalue。每当push的时候，就要pk一下，如果小于当前minvalue，才会放进minstack。如果pop的时候，pop出去的数为minstack，则更新minvalue，但如果minvalue为0，就要再次置为默认值float('inf‘).

### [lc581](src/lc581.py)
idea: Array, Shortest Unsorted Continuous Subarray，找到最短需要排序的子序列，可以使原序列使ordered
* 解法1：build一个新的ordered array，找出不一样的index
* 解法2：找出前一段的最大值和后一段的最小值，如果当前nums[i]<max,则设为end(最后一个比当前max小的值，右边不会再有比max小的情况），如果当前nums[n-1-i]>min，则设为beg(最后一个比当前min大的值，左边不会再有比min大的情况)。即分别找到前一段和后一段，最先不符合上升规律的index。

### [lc118](src/lc118.py)
idea: Array, Pascl's Triangle

### [lc38](src/lc38.py)
idea: Count and Say, Array, 快慢指针

### [lc443](src/lc443.py)
idea: String Compression, modify in-place, String，快慢指针

### [lc347](src/lc347.py)
idea: heap, Hash Table, Counter

### [lc659](src/lc659.py) TODO  buhui
idea: 

### [lc189](src/lc189.py)
idea: Array, Rotate Array, three ways, no extra space
* 解法1： 移位
* 解法2： list compression
* 解法3： 前后部分分别reverse,最后整个倒过来

### [lc26](src/lc26.py) 
idea: Array, Two pointers, 不是一个很好的题。。。

### [lc645](src/lc645.py) 
idea: Set Mismatch，Hash Table，Math

### [lc217](src/lc217.py) 
idea: Constant Duplicate，Array，Hash Table

### [lc111](src/lc111.py) 
idea: Minimum Depth of Binary Tree, BFS, Tree

### [lc107](src/lc107.py) 
idea: Binary Tree Level Order Traversal II, BFS, Tree

### [lc367](src/lc367.py) 
idea: Binary Search，Math,valid perfect square，实现sqrt

### [lc69](src/lc69.py) 
idea: Binary Search，Math，sqrt(x)

### [lc441](src/lc441.py) 
idea: Math, Binary Search, Arranging Coins

### [lc374](src/lc374.py) 
idea: Binary Search, 二分搜索，Guess Number Higher or Lower

### [lc169](src/lc169.py) 
idea: Array，Divide and Conqure，一个很厉害的算法，Majority Element(出现次数>n/2)，前提条件必须满足majority elements

### [lc35](src/lc35.py) 
idea: Array, Binary Search, Search Insert Position

### [lc744](src/lc744.py) 
idea: Binary Search, Find Smallest Letter Greater Than Target

### [lc287](src/lc287.py) 
idea: Two Pointers, Array, Binary Search, Find the Duplicate Number, 从中间开始分，冗余的一边比另一边多一些元素

### [lc349](src/lc349.py) 
idea: Set，Intersection of Two Arrays

### [lc350](src/lc350.py) 
idea: Set，Intersection of Two ArraysII, Set, Counter

### lc[3](src/lc3.py)
idea: Two pointers, String, Sliding-Window, Longest Substring Without Repeating Characters

### lc[11](src/lc11.py)
idea: Two pointers, Array, Container With Most Water, 前后夹逼，最大面积应该取决于两边的高度和距离，不停地pk

### lc[42](src/lc42.py) TODO tut'ed
idea: 

### lc[725](src/lc725.py)
idea: Linked List, 如果连接和切断linked list， Split Linked List in Parts

### lc[24](src/lc24.py)
idea: Linked List，swap nodes in pairs，每两个互换顺序，注意使用dummy，prev等

### lc[206](src/lc206.py)
idea: Linked List，Reverse Linked List, iterative and recursion

### lc[25](src/lc25.py)
idea: Reverse Nodes in k-Group, Linked List, iterative, 值得注意一点，如果dummy = prev，那么随着prev的变化，dummy的指向也就变了

### lc[328](src/lc328.py)
idea: Odd Eevn Linked List, 一个odummy，一个edummy就可以了，不要局限于非要把他们一个一个连接起来，显然不现实

### lc[19](src/lc19.py)
idea: Remove Nth Node From End of List
* 解法1： 快慢指针，fast比slow多走了n步，等到fast走到底，slow要跳过一格
* 解法2： dfs，递归，O(n)，更快，index

### lc[21](src/lc21.py)
idea: Merge Two sorted Lists,linked list，注意两个list可能长度不同

### lc[23](src/lc23.py)
idea: Merge k Sorted Lists，Linked List, Heap

### lc[83](src/lc83.py)
idea: Remove Duplicates from Sorted List, Linked List

### lc[82](src/lc82.py)
idea: Remove Duplicates from Sorted ListII, Linked List,直接删掉重复的elements

### lc[141](src/lc141.py)
idea: Linked List Cycle

### lc[142](src/lc142.py)
idea: Floyd’s cycle detection algorith/Tortoise and Hare Algorithm, Linked List, 如果linked list存在一个圈，那么快慢指针相遇后，从head出发的start和slow最终相遇的点，就是cycle的entry

### lc[234](src/lc234.py)
idea: Palindrome Linked List, Two pointers, 快慢指针，翻转后面的更容易

### lc[203](src/lc203.py)
idea: Remove Linked List Elements

### lc[160](src/lc160.py)
idea: Intersection of Two Linked Lists

### lc[599](src/lc599.py)
idea: Remove Linked List Elements

### lc[2](src/lc2.py)
idea: Add Two Numbers, linked list, list是倒序的，不需要inplace改变，进位判断比较简单， sum//=10

### lc[445](src/lc445.py)
idea: Add Two NumbersII，linked list, 没什么意思，可以直接求和，然后新建一个dummy

### lc[86](src/lc86.py)
idea: Partition List, linked list, 双指针

### lc[92](src/lc92.py)
idea: Reverse Linked List II

### lc[697](src/lc697.py)
idea: Array, Hash map, setdefault

### lc[125](src/lc125.py)
idea: Valid Palindrome, Two Pointers, string, isalnum

### lc[680](src/lc680.py)
idea: Valid PalindromeII, String

### lc[697](src/lc697.py)
idea: Array, Hash map, setdefault

### lc[686](src/lc686.py)
idea: Repeated String Match, a的结尾+开头一定在B中

### lc[459](src/lc459.py)
idea: Repeated Substring Pattern, string, 如果s是由重复的字符串t组成的，那么s一定在(s+s)[1:-1]。
* 如果S由SpSp组成，则S一定在pSpSpS中

### lc[1](src/lc1.py)
idea: Two Sum, Hash Table

### lc[15](src/lc1.py)
idea: 3 Sum, Two Pointers, 对撞指针

### lc[16](src/lc16.py)
idea: 3 Sum Closest, Two Pointers, 对撞指针, 比lc15更简单一些，因为题目设定只有唯一解

### lc[18](src/lc18.py)
idea: 4 Sum, Two Pointers, Hash Table，对撞指针, 模板

### lc[537](src/lc537.py)
idea: Complex Number Multiplication, 复数，python可以unzip返回

### lc[647](src/lc647.py)
idea: Palindromic Substrings, String, Dynamic Programming, 奇偶两种回文的可能性

### lc[383](src/lc383.py)
idea: string, counter

### lc[345](src/lc345.py)
idea: Reverse Vowels of a String, Two pointers

### lc[202](src/lc202.py)
idea: Happy Number, 如果是happy number，每个digit的平方的和加起来，组成一个新的数，循环，最后结果为1。

### lc[66](src/lc66.py)
idea: Plus One, Math, 先转成int，再用map换成list

### lc[657](src/lc657.py)
idea: Judge Route Circle, stirng, count

### lc[561](src/lc561.py)
idea: Array, Array Partition I

### lc[728](src/lc728.py)
idea: Math, self dividing numbers, 返回True如果能被n中的每一个digit整除，但是不能包括0

### lc[14](src/lc14.py)
idea: String, Longest Common Prefix

### lc[27](src/lc27.py)
idea: Remove Element, Two Pointers, 前后指针

### lc[13](src/lc13.py)
idea：Roman to Integer, Math, String

### lc[7](src/lc7.py)
idea: Reverse Integer, Math

### lc[9](src/lc9.py)
idea: Palindrome Number, 同理lc7

### lc[353](src/lc353.py)
idea: design snake game, queue, 把snake走过的痕迹放入一个deque里，头和尾巴是一起动的，直接snake.pop()就把尾巴更新了，新的头需要判断是否在boudary里或者touch到了body 

### lc[588](src/lc588.py)
idea: Design In-Memory File System,  dic里存储的是path，不可以用file，因为file的名字可能重复；如果一个文件里有content，再ls时，返回的就是该文件夹的名称，而不是空

### lc[394](src/lc394.py)
idea: Decode String, dfs, stack, 将s = "3[a]2[bc]" 展开为 "aaabcbc".
* 解法1：dfs，新建一个可以返回index的函数，如果isdigit()，就先展开[]里面的，递归下去
* 解法2：stack，s的顺序是digit+【+characters+】或者直接characters。所以，按照这个顺序去依次放入stack里面，再取出来。

### lc[48](src/lc48.py)
idea: Rotate the image/2D matrix by 90 degrees (clockwise)
 * 解法: first reverse up to down, then swap the symmetry 

### lc[238](src/lc238.py)
idea: Array，Product of Array Except Self, 一个left，1->len-1,递乘，一个right，len-2->0出发，left，right错位，最后left*right得出的就是product
 
### lc[692](src/lc692.py)
idea: heap, Top K Frequent Words, 用counter.most_common()时，不可以限制前k位，因为会有重复次数出现，题目限制答案必须是按照alphabetical顺序

### lc[451](src/lc451.py)
idea: heap, counter, Sort Characters By Frequency, 思路和lc692相同

### lc[454](src/lc454.py)
idea: 4 SUM II，hash table, 艺术级别的空间换时间，O(n^3)+O(n)space换成O(n^2)+O(n^2)space

### lc[378](src/lc378.py)
idea: Kth Smallest Element in a Sorted Matrix, heap

### lc[](src/lc.py)

### lc[](src/lc.py)

### lc[](src/lc.py)
 
 

