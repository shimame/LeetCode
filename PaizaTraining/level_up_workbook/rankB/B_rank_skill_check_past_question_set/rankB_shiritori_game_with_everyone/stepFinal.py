N, K, M = [int(x) for x in input().split()]
users = [1] * N
dic = [input() for _ in range(K)]
false_flag = 0
turn_player = 0
for i in range(M):
    s = input()
    flag = True
    if users[turn_player] == 1:
        if s[-1] == "z": # 単語の終わりがz
            flag = False
            # print("last word is z")
        if i != 0 and flag and false_flag == 0 and pre_s[-1] != s[0]: # 頭文字の判定
            flag = False
            # print("not equal")
        if flag and s in dic: # 単語リストにある
            dic.remove(s)
            false_flag = 0
        else: # 単語リストにない
            flag = False
            # print("not exist")

        if flag == False:
            users[turn_player] = 0 # ユーザを除外
            false_flag = 1
        pre_s = s
        turn_player += 1
        if turn_player > users[-1]:
            turn_player = 0
print(sum(users))
for j in range(len(users)):
    if users[j] == 1:
        print(j+1)