n = int(input())
point = 0
shopping_cart = {0:0, 1:0, 2:0, 3:0}

for _ in range(n):
    # 0 は食料品、1 は書籍、2 は衣類、3 はその他
    merchandise, price = map(int, input().split())
    shopping_cart[merchandise] += price

for key, val in shopping_cart.items():
    if key == 0:
        point += val // 100 * 5
    elif key == 1:
        point += val // 100 * 3
    elif key == 2:
        point += val // 100 * 2
    elif key == 3:
        point += val // 100 * 1

print(point)