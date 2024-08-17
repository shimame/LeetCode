class Young:
    def __init__(self, age):
        self.age = age
        self.bill = 0
    def take_food(self, price):
        self.bill += price
    def take_softdrink(self, price):
        self.bill += price
    def take_alcohol(self, price):
        pass
class Adult(Young):
    def __init__(self, age):
        super().__init__(age)
        self.alcohol = False
    def take_food(self, price):
        if self.alcohol:
            price -= 200
        self.bill += price
    def take_alcohol(self, price):
        self.bill += price
        self.alcohol = True
N, K = map(int, input().split())
customers = []
for _ in range(N):
    age = int(input())
    if age < 20:
        customer = Young(age)
    else:
        customer = Adult(age)
    customers.append(customer)

for _ in range(K):
    customer_num, order, price = input().split()
    customer_num = int(customer_num) - 1
    price = int(price)
    customer = customers[customer_num]
    if order == "food":
        customer.take_food(price)
    elif order == "softdrink":
        customer.take_softdrink(price)
    elif order == "alcohol":
        customer.take_alcohol(price)
for i in customers:
    print(i.bill)    