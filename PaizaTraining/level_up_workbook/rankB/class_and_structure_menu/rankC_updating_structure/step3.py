N = int(input())
users = []
for i in range(N):
    users.append(input().split())
    users[i][1] = int(users[i][1])
users.sort(key=lambda x: x[1])
for i in users:
    print(" ".join(map(str, i)))