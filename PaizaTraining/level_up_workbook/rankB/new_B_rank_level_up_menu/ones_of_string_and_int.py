N = int(input())
X = [int(input()) for _ in range(N)]
results = []
for i in X:
    ad = i + 1
    sub = i - 1
    head = int("1" + str(i))
    back = int(str(i) + "1")
    results.append([i, ad, sub, head, back])
ans = abs(X[0] - X[1])
for j in range(N):
    for k in range(j):
        for l in results[j]:
            for m in results[k]:
                if ans > abs(l - m):
                    ans = abs(l - m)
print(ans)