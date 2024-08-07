n = int(input())
pairs = []
for _ in range(n):
    pair = list(map(int, input().split()))
    pairs.append(pair)
pairs.sort(reverse=True) 
# pairs.sort(reverse=True,key = lambda x:(x[0], x[1]))
for i in pairs:
    print(i[0], i[1])