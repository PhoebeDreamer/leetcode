### Note on Array

* 顺时针翻转矩阵90度
    * lc[48](src/lc48.py)
    * 思路：先行颠倒，然后swap(m[i][j],m[j][i])

*  不用除法，o(n)时间 and constant space complexity，算出内积
    * Product of Array Except Self: lc[238](src/lc238.py)
    * 错位算法，left，right，一个从头出发，一个从尾巴出发
    

        ```
        Numbers:     2    3    4     5
        Lefts:            2  2*3 2*3*4
        Rights:  3*4*5  4*5    5      

        ```

        Let’s fill the empty with 1:

        ```
        Numbers:     2    3    4     5
        Lefts:       1    2  2*3 2*3*4
        Rights:  3*4*5  4*5    5     1

        ```

