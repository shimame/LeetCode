X = input()
sum = 0
for i in range(0, len(X), 8):
    sum += int(X[i:i+8])
print(sum)