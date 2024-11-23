N = int(input())
A = [int(x) for x in input().split()]
A_sum = 0
for i in range(N):
    A_sum += int(A[i])
    print(A_sum)