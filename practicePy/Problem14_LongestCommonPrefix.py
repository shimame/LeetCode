strs = ["flower","flow","flight"]
#"cir", "car"
answer = ""
l = list(zip(*strs))
for i in l:
    if len(set(i)) == 1:
      answer = answer + i[0]
print(answer)