n = int(input())
having_contact_lenses = [0] + [int(input()) for _ in range(n)]
m = int(input())
count = 0
for _ in range(m):
    r_contact, l_contact = map(int, input().split())
    if r_contact == l_contact:
        need_num = 2
    else:
        need_num = 1
    if need_num <= having_contact_lenses[r_contact] and need_num <= having_contact_lenses[l_contact]:
        having_contact_lenses[r_contact] -= 1
        having_contact_lenses[l_contact] -= 1
        count += 1
print(count)