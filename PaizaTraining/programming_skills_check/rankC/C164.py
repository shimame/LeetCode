n = int(input())
nums = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    tmp = nums[l-1]
    nums[l-1] = nums[r-1]
    nums[r-1] = tmp
if nums == sorted(nums):
    print("Yes")
else:
    print("No")