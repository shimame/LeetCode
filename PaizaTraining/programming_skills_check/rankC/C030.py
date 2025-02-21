h, w = map(int, input().split())
# 画素値が 128 以上 : 1 (白), 127 以下 : 0 (黒)
for _ in range(h):
    pixels = list(map(int, input().split()))
    ans_pixels = [0] * w
    for i in range(w):
        if pixels[i] >= 128:
            ans_pixels[i] = 1
    print(" ".join(map(str, ans_pixels)))