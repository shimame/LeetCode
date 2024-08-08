n = int(input())
user = {}
for _ in range(n):
    user[input()] = 0
m = int(input())
for _ in range(m):
    name, damage = input().split()
    damage = int(damage)
    user[name] += damage
user_dameges = sorted(user.items(), key = lambda x:x[0])
for i in user_dameges:
    print(i[1])