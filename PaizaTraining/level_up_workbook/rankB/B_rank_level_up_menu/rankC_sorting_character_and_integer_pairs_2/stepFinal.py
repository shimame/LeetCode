n = int(input())
dict = {}
for _ in range(n):
    s, d = input().split()
    if s in dict:
        dict[s] += int(d)
    else:
        dict[s] = int(d)
l = sorted(dict.items(), key=lambda x: x[1], reverse=True)
for s, d in l:
    print(s, d)