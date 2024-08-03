N = int(input())
end_times = []
for _ in range(N):
    t_i, h_i, m_i = input().split()
    hour = int(t_i[:2]) + int(h_i)
    minute = int(t_i[3:]) + int(m_i)
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour >= 24:
        hour %= 24
    end_times.append(str(hour).zfill(2) + ":" + str(minute).zfill(2))
for i in end_times:
    print(i)