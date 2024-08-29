N, K = [int(x) for x in input().split()]
S = [int(input()) for _ in range(N)]
ans = []
for i in range(K):
    A_l, A_r, B_l, B_r = [int(x) - 1 for x in input().split()]
    A_sub = max(S[A_l:A_r+1]) - min(S[A_l:A_r+1])
    B_sub = max(S[B_l:B_r+1]) - min(S[B_l:B_r+1])
    if A_sub == B_sub:
        answer = "DRAW"
    elif A_sub > B_sub:
        answer = "A"
    else:
        answer = "B"
    ans.append(answer)

for i in ans:
    print(i)