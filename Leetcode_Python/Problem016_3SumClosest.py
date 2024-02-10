class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 0:
            return []
        nums.sort()
        
        result = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            target = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return list(result)


nums = [-1,2,1,-4]
target = 1
instance = Solution()
print(instance.threeSumClosest(nums, target))