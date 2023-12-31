strs = ["flower","flow","flight"]
#"cir", "car"
answer = ""
rows = list(zip(*strs))
for i in rows:
    if len(set(i)) == 1:
      answer = answer + i[0]
    else:
       break
print(answer)