def lengthOfLastWord(s):
    answer = []
    strs =  s.split(' ')
    for i in strs:
        if i != '':
            answer.append(i)
    return len(answer[-1])

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))