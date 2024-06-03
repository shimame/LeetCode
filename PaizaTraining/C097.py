def gcd(x, y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    r = x % y
    while True:
        x, y = y, r
        r = x % y
        if r == 0:
            break
    return y

s = input().rstrip().split(' ')
answer = []
n = int(s[0])
x = int(s[1])
y = int(s[2])
both = (x * y) / gcd(x, y)

for i in range(1, n+1):      
    if i % both == 0:
        answer.append("AB")
    elif i % x == 0:
        answer.append("A")
    elif i % y == 0:
        answer.append("B")
    else :
        answer.append("N")

for i in answer:
    print(i)