# Note on Binary Search

```python
start = 0
end = n
while start+1<end:
    mid = (start+end)/2
    if nums[mid]<target:
        start = mid
    elif nums[mid]>target:
        end = mid
    else:
        看情况写start或者end=mid

if nums[start]==target:
    return start
else:
    return end
```

* 二分搜索的思路不要局限于数组上的应用
    * 具体例子：
        1. Find the Duplicate Number lc[287](src/lc287.py) 
        2. Median of Two Sorted Arrays，lc[4](src/lc4.py)
             * 限制条件，O(log (m+n))时间，因此要转化为在两个sorted数组里找Kth 
             number
             * 思路
                * 比较A的start+k/2位置与B的start+k/2位置大小，如果A[start+k/2]>B[start+k/2],则扔掉B中的前k/2个数，然后B的start+=k/2
                + 如果A或者B在start+k/2的位置没有数，则设置为float('inf)
                + 边界情况为如果A的start大于size，则返回B[start+k-1]
                + 如果k==1，则返回A[start]或者B[start]中较小的一个
        3. Median of k sorted Arrays
             *  还没想好思路
        4. [woodcut](http://www.lintcode.com/en/problem/wood-cut/#)  lt[183](src/lt183.py)
            ```
            Description:

            Given n pieces of wood with length L[i](integer array).
            Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. 
            What is the longest length you can get from the n pieces of wood? 
            Given L & k, return the maximum length of the small pieces.
            ```
            * 思路
                * 一开始很难想到二分法，因为本身L这个list就是unsorted的，要在O(Nlog(len))时间内求出，就考虑对长度二分。



 

* 如果思路太过复杂，就要思考是不是方向错了
    * 具体例子
        1. Search a 2D Matrix：lc[74](src/lc74.py)
        2. Search a 2D Matrix II：lc[240](src/lc240.py)

* 处理一下再二分搜索：
    * 具体例子
        1. Search in rotated sorted array：lc[33](src/lc33.py)
        2. Search for a Range: lc[34](src/lc34.py)