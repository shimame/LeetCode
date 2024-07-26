N, K = map(int, input().split())
A = []
T = []
for i in range(N):
    a = [int(x) for x in input().split()]
    A.append(a)

for j in range(K):
    t = []
    for k in range(N):
        t.append(A[k][j])
    T.append(t)

for l in range(K):
    print(" ".join(map(str, T[l])))


"""answer
n, k = map(int, input().split())
a = [input().split() for _ in range(n)]

for i in range(k):
    for j in range(n):
        if j == n - 1:
            print(a[j][i])
        else:
            print(a[j][i], end=" ")
"""