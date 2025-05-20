n, m, s = map(int, input().split())
musics = [list(map(int, input().split())) for _ in range(n)]
musics.sort(key=lambda x: (x[0], x[1]))
count = 0
limit_time = m * 60 + s
for i in range(n):
    music_time = musics[i][0] * 60 + musics[i][1]
    if limit_time >= music_time:
        limit_time -= music_time
        count += 1
    else:
        break

print(count)