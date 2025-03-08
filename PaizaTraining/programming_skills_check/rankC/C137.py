n = int(input())
dic1 = {}
dic2 = {}

for _ in range(n):
    name, shares = input().split()
    if name not in dic1:
        dic1[name] = 0
        dic2[name] = 0
    
    dic1[name] += 1
    dic2[name] += int(shares)

print(max(dic1, key=dic1.get))
print(max(dic2, key=dic2.get))