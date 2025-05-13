now_year, now_month, now_day = map(int, input().split())  
t_month, t_day = map(int, input().split())

next_paiza = now_year
while next_paiza % 4 != 1:
    next_paiza += 1

term_year = next_paiza - now_year
days = t_day - now_day

while now_month != t_month:
    if now_month % 2 == 0:
        days += 15
    else:
        days += 13
    
    now_month += 1

    if now_month == 14:
        now_month = 1
        term_year -= 1

days += (7 * 13 + 6 * 15) * term_year
print(days)