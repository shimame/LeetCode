s = list(input())
total = 0
for i in s:
    if i == "-":
        continue
    else:
        if i == "0":
            total += 12
        else:
            total += int(i) + 2
print(total * 2)