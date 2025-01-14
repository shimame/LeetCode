days = ["x" for _ in range(31)]

m = int(input())
for _ in range(m):
    a_day = int(input())
    days[a_day - 1] = "A"

n = int(input())
pre_dup = "B"
for _ in range(n):
    b_day = int(input())
    if days[b_day - 1] == "A":
        if pre_dup == "A":
            days[b_day - 1] = "B"
            pre_dup = "B"
        elif pre_dup == "B":
            days[b_day - 1] = "A"
            pre_dup = "A"
    else:
        days[b_day - 1] = "B"

print("\n".join(days))