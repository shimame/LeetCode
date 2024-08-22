N, X, P = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
A.extend([X, P])
A.sort()
print(A.index(P) + 1)