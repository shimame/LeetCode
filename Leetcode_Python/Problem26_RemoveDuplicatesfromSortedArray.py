def my_removeDuplicates(nums):
    for i in nums[:]:
        if pre_num == i:
            nums.remove(i)
        pre_num = i
    print(nums)
    return len(nums)
    """
    :type nums: List[int]
    :rtype: int
    """

def removeDuplicates(nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
# 1,1,2
print(removeDuplicates(nums))