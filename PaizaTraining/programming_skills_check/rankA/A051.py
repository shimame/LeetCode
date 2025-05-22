h, w = [int(x) for x in input().split()]
first = [0] + [int(y) for y in input().split()] + [0]
posi = first.index(max(first))
root_sum = max(first)
print(f"first , root = {root_sum}")
print(f"posi = {posi}")

for i in range(h-1):
    s = [0] + [int(z) for z in input().split()] + [0]
    root = max(s[posi-1:posi+2])
    print(f"i = {i} , root = {root}")
    root_sum += root
    posi += s[posi-1:posi+2].index(root) - 1
    print(f"posi = {posi}")
print(root_sum)