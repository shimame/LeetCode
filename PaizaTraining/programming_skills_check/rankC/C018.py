n = int(input())
recipe_foods = {}
for _ in range(n):
    name, amount = input().split()
    recipe_foods[name] = int(amount)

m = int(input())
having_foods = {}
for _ in range(m):
    name, amount = input().split()
    having_foods[name] = int(amount)

cooking_amounts = []

for name, amount in recipe_foods.items():
    if name not in having_foods:
        cooking_amounts.append(0)
        break
    else:
        cooking_amounts.append(having_foods[name] // amount)
print(min(cooking_amounts))