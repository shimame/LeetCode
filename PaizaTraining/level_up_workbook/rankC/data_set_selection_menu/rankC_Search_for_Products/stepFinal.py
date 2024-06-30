N, Q = map(int, input().split())
S = []
T = []
for  _ in range(N):
    S_i = input()
    S.append(S_i)
for _ in range(Q):
    T_j = input()
    if T_j in S:
        print(S.index(T_j)+1)
    else:
        print(-1)