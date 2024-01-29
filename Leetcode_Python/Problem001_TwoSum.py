class Solution(object):
    def twoSum(self, nums, target):
        nums = [2,7,11,15]
        target = 9
        answer = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                answer = num1 + num2
                if(target == answer and i < j):
                    return i,j

nums = [2,7,11,15]
target = 9
instance = Solution()
print(instance.twoSum(nums, target))