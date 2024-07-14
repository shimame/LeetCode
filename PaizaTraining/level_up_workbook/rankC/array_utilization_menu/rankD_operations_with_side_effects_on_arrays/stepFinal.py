N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = []
for i in range(N):
    if A[i] >= K:
        B.append(A[i])

for j in B:
    print(j)