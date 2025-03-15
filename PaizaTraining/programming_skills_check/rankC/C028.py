n = int(input())
point = 0
for _ in range(n):
    correct, ans = input().split()
    if len(correct) == len(ans):
        wrong = 0
        for i in range(len(correct)):
            if correct[i] != ans[i]:
                wrong += 1
        if wrong == 0:
            point += 2
        elif wrong < 2:
            point += 1
print(point)