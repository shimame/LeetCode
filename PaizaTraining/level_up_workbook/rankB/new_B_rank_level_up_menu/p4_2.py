S = input()
leet_S = S
result = "nothing"
leet = ["4", "@", "1", "!", "2"]
changed = ["a", "a", "i", "i", "z"]
for i in S:
    if i in leet:
        leet_S = leet_S.replace(i, changed[leet.index(i)])
if "paiza" in S:
    result = "paiza"
elif "paiza" in leet_S:
    result = "leet"
print(result)