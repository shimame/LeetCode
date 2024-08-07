N = int(input())
pairs = []
for _ in range(N):
    pair = list(map(int, input().split()))
    pairs.append(pair)
pairs.sort(reverse=True,key = lambda x:(x[1], x[0]))
for i in pairs:
    print(i[0], i[1])