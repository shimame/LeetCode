X, M, N = [int(i) for i in input().split()]
ans = [X % M]
for i in range(2, N+1):
    rnd_i = (X ** i + ans[i-2]) % M
    ans.append(rnd_i)
for j in ans:
    print(j)