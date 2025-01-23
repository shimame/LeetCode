ATK, DEF, AGI = [int(a) for a in input().split()]
N = int(input())
ans = []
for _ in range(N):
    evol_name, MINATK, MAXATK, MINDEF, MAXDEF, MINAGI, MAXAGI = [b for b in input().split()]
    if int(MINATK) <= ATK <= int(MAXATK) and int(MINDEF) <= DEF <= int(MAXDEF) and int(MINAGI) <= AGI <= int(MAXAGI):
        ans.append(evol_name)
if len(ans) == 0:
    print("no evolution")
else:
    print("\n".join(ans))