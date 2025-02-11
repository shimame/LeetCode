n = int(input())
min_cm = 100.0
max_cm = 200.0

for _ in range(n):
    # le(h以下) or ge(h以上), cm
    c, h = input().split()
    h = float(h)
    # 身長がわからない子供の身長がh以下の時
    if c == "le" and max_cm > h:
        max_cm = h
    # 身長がわからない子供の身長がh以上の時
    elif c == "ge" and min_cm < h:
        min_cm = h

print(min_cm, max_cm)