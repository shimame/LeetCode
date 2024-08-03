S = input()
hour = int(S[:2])
minute = int(S[3:]) + 30
if minute >= 60:
    minute -= 60
    hour += 1
print(str(hour).zfill(2) + ":" + str(minute).zfill(2))