
nums = [1,0,0,1,0,1,-1]

nums.sort()
print(nums)
if len(nums) < 3:
    print(None)

ans = []
count = 0
i = 0

while i < len(nums):  
    j=i+1  
    while j<len(nums):
        flag = False
        if -(nums[i] + nums[j]) in nums[j+1:]:
            ans.append([nums[i],nums[j],-nums[i]-nums[j]])
            count+=1 

        while j<len(nums):
            if nums[i] == nums[j]:
                i=j
                j+=1
                flag = True
            
            prev = nums[j]
            if prev = nums[j]

        

    i+=1
        

print(ans)
