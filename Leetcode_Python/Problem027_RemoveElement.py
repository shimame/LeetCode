class Solution(object):
    def removeElement(self, nums, val):
        answer = len(nums)
        count = 0
        for i in nums:
            if i != val:
                nums[count] = i
                count += 1
            else:
                answer -= 1
        return answer
    
nums = [0,1,2,2,3,0,4,2]
val = 2
instance = Solution()
print(instance.removeElement(nums, val))