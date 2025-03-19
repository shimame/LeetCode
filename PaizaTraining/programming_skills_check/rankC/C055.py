n = int(input())
g = input()
flag = False

for _ in range(n):
    s = input()
    if g in s:
        print(s)
        flag = True

if not flag:
    print("None")