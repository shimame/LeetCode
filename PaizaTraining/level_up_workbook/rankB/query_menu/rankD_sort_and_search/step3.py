N, Q = [int(x) for x in input().split()]
A = {int(input()) for _ in range(N)}
for i in range(Q):
    K_i = int(input())
    if K_i in A:
        print("YES")
    else:
        print("NO")