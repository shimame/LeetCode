def battle_check(my_level, enemy_level):
    if my_level == enemy_level:
        pass
    elif my_level > enemy_level:
        my_level += enemy_level // 2
    else:
        my_level = my_level // 2
    return my_level

n, l = [int(i) for i in input().split()]
for x in range(n):
    enemy_level = int(input())
    l = battle_check(l, enemy_level)
print(l)