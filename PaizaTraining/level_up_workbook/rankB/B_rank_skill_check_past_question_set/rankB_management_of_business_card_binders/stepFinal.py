n, m = [int(x) for x in input().split()]
q = (m - 1) // (2 * n) + 1
sum = 2 * n * (2 * q - 1) + 1
ans = sum - m
print(ans)

# q * 2 * n + 1
# 8 11
# 19
# 3 * 6 + 1
