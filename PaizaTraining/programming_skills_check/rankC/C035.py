n = int(input())
win_count = 0

for _ in range(n):
    input_line = input().split()
    t = input_line[0]
    total_score = sum(list(map(int, input_line[1:])))
    if input_line[0] == "s":
        score = int(input_line[2]) + int(input_line[3])
    else:
        score = int(input_line[4]) + int(input_line[5])
    if score >= 160 and total_score >= 350:
        win_count += 1

print(win_count)