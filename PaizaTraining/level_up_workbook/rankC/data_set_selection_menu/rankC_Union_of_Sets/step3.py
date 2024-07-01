N = int(input())
A = [int(x) for x in input().split()]
for i in range(1, len(A)):
    if A[i] in A[:i]:
        print("Yes")
    else:
        print("No")