N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
for i in range(N):
    print(A[i] - B[i])