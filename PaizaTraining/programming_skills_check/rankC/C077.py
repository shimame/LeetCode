k, n = map(int, input().split())
point = 100 // n

for _ in range(k):
    d, a = map(int, input().split())
    score = point * a
    if d <= 0:
        pass
    elif d < 10:
        score = score * 8 // 10
    else:
        score = 0
    
    if score >= 80:
        eval = "A"
    elif score >= 70:
        eval = "B"
    elif score >= 60:
        eval = "C"
    else:
        eval = "D"
    print(eval)