key_life = list(map(int, input().split()))
sentence = input()
ans = []
for i in range(len(sentence)):
    if key_life[ord(sentence[i]) - 97] > 0:
        ans.append(sentence[i])
        key_life[ord(sentence[i]) - 97] -= 1
print("".join(ans))