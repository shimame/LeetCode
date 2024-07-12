N, M, K, L = map(int, input().split())
a = []
for i in range(N):
    a.append(input().split())
print(a[K - 1][L - 1])