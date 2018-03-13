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
    * 具体例子，[lc287](src/lc287.py) Find the Duplicate Number
