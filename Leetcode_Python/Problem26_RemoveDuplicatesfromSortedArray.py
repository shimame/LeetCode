def removeDuplicates(nums):
    neo = list(set(nums))
    neo.sort()
    del nums[:]
    nums += neo
    return len(nums)

nums = [1,1,2]
# 0,0,1,1,1,2,2,3,3,4
print(removeDuplicates(nums))