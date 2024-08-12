P_HP = int(input()) - 2
turn = 2
P_damage_n_1 = 1
P_damage_n_2 = 1
M_damage_n_1 = 1
M_damage_n_2 = 1
while P_HP > 0:
    turn += 1

    P_magic = P_damage_n_1 + P_damage_n_2

    M_magic = M_damage_n_1 * 2 + M_damage_n_2
    P_HP -= M_magic

    M_damage_n_2 = M_damage_n_1
    M_damage_n_1 = P_magic
    P_damage_n_2 = P_damage_n_1
    P_damage_n_1 = M_magic
print(turn)