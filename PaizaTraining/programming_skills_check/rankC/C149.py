S = list(input())
T = list(input())
upper_s = []

for i in S:
    if i.isupper():
        upper_s.append(i)

for j in range(len(T)):
    if T[j].upper() in upper_s:
        T[j] = T[j].upper()
    else:
        T[j] = T[j].lower()

print("".join(T))