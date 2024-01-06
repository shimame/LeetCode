def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[i + m] = nums2[i]
    nums1.sort()
    return nums1
    

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
print(merge(nums1, m, nums2, n))