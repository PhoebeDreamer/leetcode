### Note on Array

* prefix sum
    * sum(i~j) = sum[j]-sum[i-1]
    * 求两个变量的搭配最优
    ```
    for 其中一个数
        让另外一个数最优
    ```
    * 实例：
        1. Maximum subarray: lc[53](src/lc53.py) 
        2. Minimum subarray: lc[44](src/lc44.py)
        3. Maximum subarrayII: lt[42](src/lt42.py)
        4. best time to buy and sell stock: lc[121](src/lc121.py)
        5. Maximum Product Subarray: lc[152](src/lc152.py)
        6. Subarray Product Less Than K: lc[713](src/lc713.py)
        7. Minimum Size Subarray Sum: lc[209](src/lc209.py)
        8. Subarray Sum Equals K: lc[560](src/lc560.py)
    