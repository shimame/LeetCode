N, M = [int(x) for x in input().split()]
A = [int(n) for n in input().split()]
addtion = [0] * (N+1)

# imos法
for _ in range(M):
    l, u, a = [int(n) for n in input().split()]
    addtion[l-1] += a
    addtion[u] -= a #範囲外で打ち消し合う

for i in range(N):
    print(A[i] + addtion[i])
    addtion[i+1] += addtion[i]