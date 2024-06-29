H, W, r, c = map(int, input().split())
for i in range(H):
    input_line = input()
    if i == r - 1:
        search_line = list(input_line)
if search_line[c-1] == "#":
    print("Yes")
else:
    print("No")


"""answer
H, W, r, c = map(int, input().split())
maze = [input() for _ in range(H)]

if maze[r-1][c-1] == "#":
    print("Yes")
else:
    print("No")
"""