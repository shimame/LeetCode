n = int(input())
user = {}
for _ in range(n):
    user[input()] = 0
m = int(input())
for _ in range(m):
    name, damage = input().split()
    damage = int(damage)
    user[name] += damage
S = input()
print(user[S])