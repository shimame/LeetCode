N, K, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
employee = []

A.sort(reverse=True)
del A[:M]
for i in A:
    if i >= K:
        employee.append(i)

print(len(employee))

"""answer
n, k, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    if i >= k:
        ans += 1
ans -= m
if ans < 0:
    ans = 0

print(ans)
"""