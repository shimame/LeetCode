def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    answer = 0.0
    nums = nums1 + nums2
    nums.sort()
    half = len(nums) // 2
    if len(nums) % 2 == 0:
        answer = ((nums[half - 1]) + (nums[half])) / 2
    else:
        answer = nums[half]
    return answer

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))