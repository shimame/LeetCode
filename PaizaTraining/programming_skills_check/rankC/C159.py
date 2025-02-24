n, k = map(int, input().split())
winning_nums = list(map(int, input().split()))
voted_nums = list(map(int, input().split()))
ans = []
for i in range(k):
    if voted_nums[i] in winning_nums:
        ans.append(i+1)

if len(ans) == 0:
    print(-1)
else:
    print("\n".join(map(str, ans)))