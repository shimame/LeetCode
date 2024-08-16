N = int(input())
users = []
for _ in range(N):
    users.append(input().split())
for i in users:
    print("User{")
    print("nickname : " + i[0])
    print("old : " + i[1])
    print("birth : " + i[2])
    print("state : " + i[3])
    print("}")