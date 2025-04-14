a, b = map(int, input().split())
b_flag = False

for c in range(10):
    for d in range(10):
        if (c * 10 + d) * d == a * 100 + c * 10 + b:
            print(c, d)
            b_flag = True
            break
    if b_flag:
        break

if not b_flag:
    print("No")