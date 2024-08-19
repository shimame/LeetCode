class Attack:
    def __init__(self, frame, damage):
        self.frame = frame
        self.damage = damage

class Player:
    def __init__(self, hp, at1, at2, at3):
        self.hp = hp
        self.at1 = at1
        self.at2 = at2
        self.at3 = at3
    
    #技の選択
    def select_attack(self, num):
        if num == 1:
            use_at = self.at1
        elif num == 2:
            use_at =  self.at2
        elif num == 3:
            use_at =  self.at3
        return use_at

    #技の強化
    def enhance(self):
        if self.at1.frame != 0 and self.at1.damage != 0:
            self.at1.frame -= 3
            self.at1.damage += 5
            if self.at1.frame <= 0:
                self.at1.frame = 1
        if self.at2.frame != 0 and self.at2.damage != 0:
            self.at2.frame -= 3
            self.at2.damage += 5
            if self.at2.frame <= 0:
                self.at2.frame = 1
        if self.at3.frame != 0 and self.at3.damage != 0:
            self.at3.frame -= 3
            self.at3.damage += 5
            if self.at3.frame <= 0:
                self.at3.frame = 1
#攻撃の処理
def battle_process(pl1, pl2, at1, at2):
    if pl1.hp <= 0 or pl2.hp <= 0:
        return
    attack1 = pl1.select_attack(at1)
    attack2 = pl2.select_attack(at2)
    if attack1.frame < attack2.frame:
        if attack1.frame == 0 and attack1.damage == 0:
            pl1.enhance()
            if attack2.frame != 0 and attack2.damage != 0:
                pl1.hp -= attack2.damage
        else:
            pl2.hp -= attack1.damage
    elif attack1.frame > attack2.frame:
        if attack2.frame == 0 and attack2.damage == 0:
            pl2.enhance()
            if attack1.frame != 0 and attack1.damage != 0:
                pl2.hp -= attack1.damage
        else:
            pl1.hp -= attack2.damage
    

N, K = [int(x) for x in input().split()]
players = []
for _ in range(N):
    hp, f1, d1, f2, d2, f3, d3 = [int(x) for x in input().split()]
    at1 = Attack(f1, d1)
    at2 = Attack(f2, d2)
    at3 = Attack(f3, d3)
    players.append(Player(hp, at1, at2, at3))
sum_pl = len(players)

for _ in range(K):
    pl_num1, at1, pl_num2, at2 = [int(x) for x in input().split()]
    pl1, pl2 = players[pl_num1 - 1], players[pl_num2 - 1]
    battle_process(pl1, pl2, at1, at2)

for i in players:
    if i.hp <= 0:
        sum_pl -= 1
print(sum_pl)