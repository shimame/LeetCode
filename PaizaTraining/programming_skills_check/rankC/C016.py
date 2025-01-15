s = list(input())
dict = {"A": "4",
        "E": "3",
        "G": "6",
        "I": "1",
        "O": "0",
        "S": "5",
        "Z": "2"
}

for i in range(len(s)):
    if s[i] in dict:
        s[i] = dict[s[i]]

print("".join(s))