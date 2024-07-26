N = int(input())
A = [int(x) for x in input().split()]
B = []
for i in range(N):
    b =[]
    for j in range(N):
        b.append(A[i] * A[j])
    print(" ".join(map(str, b)))