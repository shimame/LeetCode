N, K = map(int, input().split())
users = []
for _ in range(N):
    users.append(input().split())
for _ in range(K):
    input_line = input().split()
    user_num = int(input_line[0])
    users[user_num - 1][0] = input_line[1]
for i in users:
    print(" ".join(i))