import math
s = input().rstrip().split(' ')
answer = ["N"]
n = int(s[0])
x = int(s[1])
y = int(s[2])
both = math.lcm(x, y)
print(both) #ここが直さないといけない
for i in range(2, n+1):      
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