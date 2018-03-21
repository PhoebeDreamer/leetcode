# Note on tag TwoPointers

* k-sum类的题， 都可以转化为two-sum的解法。
    * 实例：
        1. 2sum [lc1](src/1.py)
        2. 3Sum [lc15](src/lc15.py)
            + 转换为2sum，对撞指针
        3. 4Sum [lc18](src/lc18.py)
            * 典型空间换时间例子
        4. kSum
        5. 3Sum Closest：[lc16](src/lc16.py)
    * 思考：
        * 在4Sum那个题中，如果直接用模板，时间是O(N^K-1)，为了平衡时间，我们可以考虑转变为2sum和2sum的问题，用空间来换时间
    * 模板
    ```python
    def findNsum(num, N, target, partial, result):
        if N<2 or len(nums)>N or target<nums[0]*N or target>nums[-1]*N:
            return
        if N==2:
            start, end = 0, len(nums)-1
            while start<end:
                if nums[start]+nums[end]<target: start+=1
                elif nums[start]+nums[end]>target: end-=1
                else:
                    result.append(partial+[nums[start], nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]: start+=1
                    while start<end and nums[end]==nums[end+1]: end-=1
        else:
            for i in range(len(nums)-n+1):
                if i==0 or (i>0 and nums[i]!=nums[i-1]):
                    findNsum(nums[i+1:], N-1, target-nums[i], partial+[nums[i]], result )
    ```
* sliding-Window, 前后指针
    * 实例：
        1. [lc438](src/lc438_rick.py)， 
        2. lc[3](src/lc3.py)
        3. Minimum Size Subarray Sum： lc[209](src/lc209.py)
            * 值得思考别人的思路，有的时候判断的方式不必那么保守，也可以倒着

* 对撞指针，两端夹击
    * 实例：
        1. Container With Most Water: lc[11](src/lc11.py)
        2. Reverse Vowels of a String: lc[345](src/lc345.py)