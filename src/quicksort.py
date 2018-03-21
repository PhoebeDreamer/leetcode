def quicksort(nums):
    if len(nums)<=1:
        return nums
    
    def _quicksort(nums, start, end):
        if start>=end:
            return 
        pivot = partition(nums, start, end)
        _quicksort(nums, start, pivot-1)
        _quicksort(nums, pivot+1, end)
        
    return _quicksort(nums, 0, len(nums)-1)

def partition(nums, start, end):
    pivot = start
    for i in range(start+1, end+1):
        if nums[i]<=nums[start]:
            pivot+=1
            nums[i], nums[pivot] = nums[pivot], nums[i]
    nums[pivot], nums[start] = nums[start], nums[pivot]

    return pivot

def partition1(nums, start, end):
    k = nums[start]
    i, j = start+1, end
    while i<=j:
        while i<=j and nums[i]<=k: i+=1
        while i<=j and nums[j]>k: j-=1
        
        if i<=j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1

    nums[start], nums[i-1] = nums[i-1], nums[start]
    return i-1


nums = [0,1,0,1,0,9,2,3,0,2,0,2,6,59,2,3,5,6,2,56,7,2,1,5,3,2,6,7,4,3,1,5,7,8,5,3,2]
quicksort(nums)
print(nums)