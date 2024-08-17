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
count = 0
for _ in range(N):
    age = int(input())
    if age < 20:
        customer = Young(age)
    else:
        customer = Adult(age)
    customers.append(customer)

for _ in range(K):
    input_line = input().split()
    customer_num = int(input_line[0]) - 1
    order = input_line[1]
    customer = customers[customer_num]
    if order == "A":
        print(customer.bill)
        count += 1
    elif order == "0":
        customer.take_alcohol(500)
    else:
        price = int(input_line[2])
        if order == "food":
            customer.take_food(price)
        elif order == "softdrink":
            customer.take_softdrink(price)
        elif order == "alcohol":
            customer.take_alcohol(price)
print(count)