l, m, s = map(int, input().split())
n = int(input())
bookshelves = [list(map(int, input().split())) for _ in range(n)]
min_price = 100001
for i in range(n):
    price, l_storage, m_storage, s_storage = bookshelves[i]
    if price < min_price:
        if l <= l_storage:
            space_storage = l_storage - l
            if m <= m_storage + space_storage:
                space_storage += m_storage - m
                if s <= s_storage + space_storage:
                    min_price = price
if min_price == 100001:
    print(-1)
else:
    print(min_price)