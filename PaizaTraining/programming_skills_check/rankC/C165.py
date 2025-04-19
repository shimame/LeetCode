n = int(input())
foods = input().split()
c = []
r = []

for i in range(n):
    if foods[i] == "C":
        c.append(i+1)
    elif foods[i] == "R":
        r.append(i+1)

curry_rice_count = min(len(c), len(r))
print(curry_rice_count)

for j in range(curry_rice_count):
    print(c[j], r[j])