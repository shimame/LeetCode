A, B = map(int, input().split())
rotate_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

count = 0
for i in range(A, B+1):
    num = str(i)
    
    if any(i not in rotate_map for i in num):
        continue

    rotated = "".join(rotate_map[i] for i in reversed(num))
    
    if num == rotated:
        count += 1

print(count)