t = input().split()
month, day = map(int, t[0].split('/'))
hour, minute = map(int, t[1].split(':'))
plus_day = hour // 24
hour = hour % 24
day += plus_day
print(str(month).zfill(2) + '/' + str(day).zfill(2) + ' ' + str(hour).zfill(2) + ':' + str(minute).zfill(2))