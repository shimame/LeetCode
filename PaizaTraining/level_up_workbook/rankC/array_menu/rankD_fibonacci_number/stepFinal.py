N = int(input())
F = []

for i in range(N):
    if i == 0:
        F.append(0)
    elif i == 1:
        F.append(1)
    else:
        num = F[-1] + F[-2]
        F.append(num)
    print(F[-1])