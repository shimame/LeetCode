def product_nums(nums):
    result = 1
    for num in nums:
        result *= num
    return result

n = int(input())
nums = list(map(int, input().split()))
max_pro = -float('inf')

for i in range(n):
    for j in range(n):
        if i != j:
            check_nums = nums[:]
            check_nums[i] += 1
            check_nums[j] -= 1
            pro = product_nums(check_nums)
            if pro > max_pro:
                max_pro = pro
print(max_pro)