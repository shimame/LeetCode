S = input()
l = []
for i in range(len(S)):
    if S[i] not in l:
        l.append(S[i])
print("".join(l))

"""answer
s = input()

st = set()
for ele in s:
    if ele not in st:
        st.add(ele)
        print(ele, end="")
"""