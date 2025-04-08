a, op, b, eq ,c = input().split()

if a == "x":
    b, c = int(b), int(c)
    if op == "+":
        ans = c - b
    elif op == "-":
        ans = c + b
elif b == "x":
    a, c = int(a), int(c)
    if op == "+":
        ans = c - a
    elif op == "-":
        ans = (c - a) * -1
elif c == "x":
    a, b = int(a), int(b)
    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
print(ans)