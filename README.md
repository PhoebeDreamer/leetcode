# phoebe leetcode
This is my leetcode practice book.

### [lc438](src/lc438.py) TODO

### [lc437](src/lc437.py) TODO

### [lc377](src/lc377.py) TODO

### [lc130](src/lc130.py) TODO

### [lc332](src/lc332.py) TODO


### [lc101](src/lc101.py) TODO
idea: Tree, DFS, BFS, 判断书是否对称
* dfs:由basic case往下推，1个node只需要判断left,right是否相同；两个node需要判断left.left与right.right，left.right与right.left;更多node的时候，最左边，最右边（依次往内）判断是否对称【边际到中央】
* bfs：利用stack，push进去left，right，情况较为复杂

### [lc226](src/lc226.py) TODO
idea: Tree, recursion, invert Binary Tree

### [lc22](src/lc22.py)
idea: backtracking，随机组合的顺序有限定

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
idea: Divide and Conquer, 分治法, 复杂的地方在于怎么处理重复的情况，因此不仅要有left，right，还要有equal

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

### [lc98](src/lc98.py)
idea：

### [lc230](src/lc230.py)
idea：BST, Tree, find the k smallest element in BST, 利用BST的性质，root.left<root, root.right>root.

### [lc501](src/lc501.py)
idea：Tree, dfs, stcak, 

### [lc669](src/lc669.py) important!!!
idea: DFS, Tree，node如果小于min，则返回node.right;node如果大于max，则返回node.left；同时对】node.left和node.right进行递归

### [lc547](src/lc547.py) important!!!!!!!!!
idea: DFS, path标记，找到朋友圈个数，突破点在如果是两个独立的朋友圈a、b，则a绝不会出现在b所在的行或列上，即如果a出现在b所在行上，两者一定属于同一个朋友圈。
* 因为一开始只关注了怎么标记原二维数组，所以越写越乱 눈_눈

### [lc112](src/lc112.py)
idea: DFS, Tree. 判断是否存在一条路径从root出发直到最子叶，和为target。逆向思维，往下递归时，target减去已经走过的node.val，判断当为最子叶（not root.left and not root.right)时，target是否和node.val相同。

### [lc113](src/lc113.py)
idea: DFS, Tree. Path SumII，同理lc112，只是函数多加了一个partial参数，因为要记录走过的路径。


