N, M = map(int, input().split())
products = {}
for _ in range(N):
    A_i, B_i = input().split()
    products[A_i] = B_i
for _ in range(M):
    S_j = input()
    if S_j in products:
        print(products[S_j])
    else:
        print(-1)