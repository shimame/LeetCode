S = input()
try:
    int(S)
    print("YES")
except ValueError:
    print("NO")

"""answer
s = input()

if s.isdigit():
    print("YES")
else:
    print("NO")
"""