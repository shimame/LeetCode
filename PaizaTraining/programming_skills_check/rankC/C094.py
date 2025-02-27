def calculation_tax(money):
    tax = 0
    if money > 1500000:
        tax += int((money - 1500000) * 0.4)
        money = 1500000
    if money > 750000:
        tax += int((money - 750000) * 0.2)
        money = 750000
    if money > 100000:
        tax += int((money - 100000) * 0.1)
    return tax

n = int(input())
total_tax = 0
for i in range(n):
    earnings = int(input())
    total_tax += calculation_tax(earnings)
print(total_tax)