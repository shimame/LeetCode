s = input()
t = input()
if s == t:
    ans = "NO"
else:
    ans = "YES"
    set_s = set(s)
    for i in set_s:
        if s.count(i) != t.count(i):
            ans = "NO"
            break
print(ans)