n, m = map(int, input().split())
s = input()
nums = []
ans = ['0'] * m

for i in range(n // m + 1):
    num = s[i*m:i*m+m]
    nums.append(num)
if len(nums[-1]) < m:
    nums[-1] = nums[-1].ljust(m, "0")

for j in range(len(nums)):
    for k in range(m):
        if nums[j][k] == '1' and ans[k] == '0':
            ans[k] = '1'
        elif nums[j][k] == '1' and ans[k] == '1':
            ans[k] = '0'
print("".join(ans))