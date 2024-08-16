N = int(input())
users = []
for _ in range(N):
    users.append(input().split())
K = input()
for i in users:
    if i[1] == K:
        print(i[0])