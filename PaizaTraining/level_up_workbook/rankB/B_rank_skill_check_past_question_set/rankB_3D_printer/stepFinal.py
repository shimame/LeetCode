X, Y, Z = [int(i) for i in input().split()]
d = []
ans = []
for _ in range(Z):
    data = []
    for _ in range(X):
        row = input()
        data.append(row)
    input()
    d.append(data)
t_d = list(zip(*d))
print(t_d)
for i in range(Z):
    ans_row = []
    for j in range(Y):
        row = t_d[j][i]
        print(f"{i},{j} row={row}")
        if row == "." * X:
            ans_row.append(".")
        else:
            ans_row.append("#")
    ans.append("".join(ans_row))
print(ans)
for k in reversed(ans):
    print(k)
"""
3 26 5
............#.............
......#..#.....#####......
#.....................#..#
--
............#.............
......#..#......#.........
#.....................#..#
--
............#.............
......####.......#........
####..................####
--
............#.............
......#..#........#.......
#..#..................#..#
--
............#.............
......####.....#####......
####..................####
--
"""