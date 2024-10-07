c = input()
s = input()
count = 0
for i in range(len(s)-len(c)+1):
    if s[i:i+len(c)] == c:
        count += 1
print(count)