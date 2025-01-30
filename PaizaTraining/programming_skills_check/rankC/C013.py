disliked_num = input()
num = int(input())
ans = []
for _ in range(num):
    room_num = input()
    if disliked_num not in room_num:
        ans.append(room_num)

if len(ans) == 0:
    print("none")
else:
    print("\n".join(ans))