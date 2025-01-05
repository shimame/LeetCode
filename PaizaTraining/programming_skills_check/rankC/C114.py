n = int(input())
pre = list(input())
now = ""
error = ""

for _ in range(n-1):
    now = list(input())
    if pre[-1] != now[0] and error == "":
        error = pre[-1] + " " + now[0]
    pre = now

if error == "":
    print("Yes")
else:
    print(error)