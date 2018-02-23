# nums = [1,2,3,3]

# mean = sum(nums)/len(nums)
# comp = len(nums)//2
# flag = 1 if mean > comp else -1
    
# for left in range(len(nums)):
#     if flag*(nums[left]-comp) > 0 and nums[left] in nums[left+1:]:
#         print(nums[left])
#         break

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        diff = sum(nums)-sum(range(len(nums)))
        mean = sum(range(len(nums)))/(len(nums)-1)
        flag = 1 if diff >= mean else -1
        
        # mean = sum(nums)/len(nums)
        # comp = sum(range(len(nums)))//(len(nums)-1)
        # print(mean, comp)
        # flag = 1 if mean >= comp else -1
            
        for left in range(len(nums)):
            if flag*(nums[left]-mean) >= 0 and nums[left] in nums[left+1:]:
                print(nums[left])
                break
                return nums[left]
        return 'darn!'

def main():
    Solution().findDuplicate([3,2,2,2,4])

if __name__ == '__main__':
    main()            