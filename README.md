# phoebe leetcode
This is my leetcode practice book.

### [lc438](src/lc438_rick.py)
idea: hash table, sliding-window, Counter，滑动窗口。使用Counter时的技巧是，为了避免出现超时的情况，不应该对每一个窗口进行一次Counter操作，而是处理掉上一个窗口的第一个元素，如果处理后，Counter中该元素个数为0，则del。然后窗口往后移动一步，对最新的元素进行操作。

### [lc241](src/lc241.py) TODO
idea: Divide and Conquer 

### [lc437](src/lc437.py) TODO
idea: 

### [lc377](src/lc377.py) TODO
idea: 

### [lc567](src/lc567.py) TODO
idea: 待修改， Two Pointers， Sliding window， 类似438

### [lc617](src/lc617.py)
idea: Merge Two Binary Trees, Tree, preorder

### [lc226](src/lc226.py) TODO
idea: Tree, recursion, invert Binary Tree

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

### [lc630](src/lc630.py) TODO
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
idea1: Divide and Conquer, 分治法, 复杂的地方在于怎么处理重复的情况，因此不仅要有left，right，还要有equal
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
idea: DFS, Divide and Conquer，找到中间值做root，然后迭代，继续往下分

### [lc129](src/lc129.py)
idea: DFS, 类似lc257

### [lc94](src/lc94.py)
idea: inorder, dfs, stack，中序遍历，如何用iteratively实现

### [lc501](src/lc501.py) TODO
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

### [lc101](src/lc101.py) TODO
idea: Tree, DFS, BFS, 判断树是否对称，lc100的进阶版
* dfs:由basic case往下推，1个node只需要判断left,right是否相同；两个node需要判断left.left与right.right，left.right与right.left;更多node的时候，最左边，最右边（依次往内）判断是否对称【边际到中央】
* bfs：利用stack，push进去left，right，情况较为复杂