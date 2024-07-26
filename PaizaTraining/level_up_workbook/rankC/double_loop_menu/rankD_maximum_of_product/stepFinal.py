N, K = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
ans = A[0] * B[0]

for i in range(N):
    for j in range(K):
        pro = A[i] * B[j]
        if pro > ans:
            ans = pro
print(ans)