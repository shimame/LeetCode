# 種類 N と休暇のローテンションが一周するまでの日数D
n, d = [int(a) for a in input().split()]
stone_need_people = [0] + [int(b) for b in input().split()]
stone_need_people.sort()

participants = [int(c) for c in input().split()]
participants.sort()

amount_need_people = [0] * (n + 1)
stone_amount = 0

for i in range(1, n+1):
    amount_need_people[i] = amount_need_people[i-1] + stone_need_people[i]

j = 0
for k in range(d):
    while j < (n+1) and participants[k] >= amount_need_people[j]:
        j += 1
    j -= 1
    stone_amount += j

print(stone_amount)