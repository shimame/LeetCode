N = int(input())
input_lines = [input() for _ in range(N)]
set_lines = list(set(input_lines))
set_lines.sort()
counts = [0] * len(set_lines)

for i in range(len(input_lines)):
    for j in range(len(set_lines)):
        if input_lines[i] == set_lines[j]:
            counts[j] += 1

for k in range(len(set_lines)):
    print(f"{set_lines[k]} {counts[k]}")


"""answer
N = int(input())
count = {}

for _ in range(N):
    s = input()
    if s not in count:
        count[s] = 1
    else:
        count[s] += 1

for word, times in sorted(count.items()):
    print(word, times)
"""