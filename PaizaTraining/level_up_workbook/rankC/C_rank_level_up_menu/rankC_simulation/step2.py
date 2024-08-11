n = int(input())
a, b = map(int, input().split())
p = k = 1
turn = "p"
count = 0
while n >= k:
    if turn == "p":
        k += p * a
        count += 1
        turn = "k"
    else:
        p += k % b
        turn = "p"
print(count)