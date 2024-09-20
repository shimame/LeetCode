N = int(input())
ok_count = [0] * 4
ng_count = [0] * 4
tests = ["TA", "TB", "TC", "TD"]
result = ""
for _ in range(N):
    t, j = input().split()
    index = tests.index(t)
    if ng_count[index] != 2:
        if j == "ok":
            ok_count[index] += 1
        elif j == "ng":
            ng_count[index] += 1

for j in range(3, -1, -1):
    if ok_count[j] >= 2:
        result = tests[j].strip("T")

if result == "":
    result = "E"
print(result)