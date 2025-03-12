n = int(input())
users = []

for _ in range(n):
    input_line = input()
    posi = 0
    for i in range(len(input_line)-1, -1, -1):
        if not input_line[i].isdigit():
            posi = i + 1
            break
    name, num = input_line[:posi], int(input_line[posi:])
    users.append((name, num))

users.sort(key=lambda x: x[1])

for name, num in users:
    print(name + str(num))