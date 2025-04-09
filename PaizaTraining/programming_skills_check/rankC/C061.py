a, b = map(int, input().split())
a_hun, b_hun = a // 100, b // 100
a_ten, b_ten = a // 10, b // 10
a_one, b_one = a % 10, b % 10
hun_num = str((a_hun + b_hun) % 10)
ten_num = str((a_ten + b_ten) % 10)
one_num = str((a_one + b_one) % 10)
if len(str(a)) == 2 and len(str(b)) == 2:
    print(ten_num + one_num)
else:
    print(hun_num + ten_num + one_num)