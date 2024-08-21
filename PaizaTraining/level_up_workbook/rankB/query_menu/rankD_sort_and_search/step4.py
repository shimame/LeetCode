N = int(input())
A = [int(input()) for _ in range(N)]
del A[0]
for i in A:
    print(i)