N, K, Q = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
A.insert(K, Q)
for i in A:
    print(i)