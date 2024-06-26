N = int(input())
A = input().split(" ")
Q = int(input())
B = input().split(" ")
for i in range(Q):
    print(A[int(B[i])-1])