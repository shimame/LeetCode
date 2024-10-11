n = int(input())
users = {}
fortunes = {}
for _ in range(n):
    name, blood = input().split()
    users[name] = blood
m = int(input())
for _ in range(m):
    blood, result = input().split()
    fortunes[blood] = result
l = users.items()
for name, blood in l:
    print(name, fortunes[blood])