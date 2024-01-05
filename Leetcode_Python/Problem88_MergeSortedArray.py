def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    for i in range(len(nums1) - m):
       del nums1[-1]
    for i in range(n):
        for j in range(len(nums1)):
            if nums1[j] > nums2[i]:
                nums1.insert(j, nums2[i])
                print(f"j = {j},   nums2[{i}] = {nums2[i]}")
            elif j == len(nums1) - 1:
                nums1.append(nums2[i])
    if len(nums1) == 0:
        nums1 += nums2
    return nums1
    

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
print(merge(nums1, m, nums2, n))