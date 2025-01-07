n = int(input())
pre = 1
sum_diff = 0
for _ in range(n):
    now = int(input())
    diff = abs(now - pre)
    sum_diff += diff
    pre = now
print(sum_diff)