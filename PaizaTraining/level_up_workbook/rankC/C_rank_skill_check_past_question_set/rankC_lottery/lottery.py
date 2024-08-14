b = int(input())
n = int(input())
results = []
for _ in range(n):
    num = int(input())
    if b == num:
        prize = "first"
    elif b - 1 == num or b + 1 == num:
        prize = "adjacent"
    elif (b - num) % 10000 == 0:
        prize = "second"
    elif (b - num) % 1000 == 0:
        prize = "third"
    else:
        prize = "blank"
    results.append(prize)
for i in results:
    print(i)