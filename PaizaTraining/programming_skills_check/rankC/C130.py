n = int(input())
ans = []
for i in range(1, n+1):
    a, b = input().split()
    if a == "n" or b == "n":
        ans.append(i)

print(len(ans))
print("\n".join(map(str, ans)))