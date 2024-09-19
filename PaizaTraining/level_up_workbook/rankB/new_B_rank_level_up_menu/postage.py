y, x, h = [int(i) for i in input().split()]
l = [0] + [int(i) for i in input().split()]
m = [0] + [int(i) for i in input().split()]
postage = 0
if h <= l[1]:
    if max(y, x) <= l[2]:
        postage = m[1]
    elif y + x <= l[3]:
        postage = m[2]
    else:
        postage = m[3]
else:
    if max(y, x, h) <= l[4]:
        postage = m[4]
    elif y + x + h <= l[5]:
        postage = m[5]
    else:
        postage = y * x * h * m[6]
print(postage)