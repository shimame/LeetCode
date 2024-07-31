N = int(input())
flag = 0
for a in range(1, N - 1):
    for b in range(1, N - a):
        c = N - a - b
        if a * a == b * b + c * c:
            flag = 1
            break
    else:
        continue
    break
if flag == 1:
    print("YES")
else:
    print("NO")