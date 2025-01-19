n = int(input())
names = {}
for _ in range(n):
    name = input()
    if name not in names:
        names[name] = 1
    else:
        names[name] += 1
print(max(names, key=names.get))