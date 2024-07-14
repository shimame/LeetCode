N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

for i in range(N):
    print(A[i] + K)