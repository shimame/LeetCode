n, k = [int(x) for x in input().split()]
nums = [int(y) for y in input().split()]
sums = [0] * (n-k+1)
sums[0] = sum(nums[:k])

for i in range(1, n-k+1):
    sums[i] = sums[i-1] - nums[i-1] + nums[i+k-1]

max_num = max(sums)
print(sums.count(max_num), sums.index(max_num)+1)