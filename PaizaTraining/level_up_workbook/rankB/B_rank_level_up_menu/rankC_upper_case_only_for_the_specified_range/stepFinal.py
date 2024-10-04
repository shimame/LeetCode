a, b = [int(x) for x in input().split()]
s = input()
s = s[:a-1] + s[a-1:b].upper() + s[b:]
print(s)