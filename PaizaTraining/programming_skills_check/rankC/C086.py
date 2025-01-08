s = input()
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
ans = [i for i in s if i not in vowel]
print("".join(ans))