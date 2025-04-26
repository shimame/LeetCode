s, a, b = map(int, input().split())
price = s

while True:
    price += 10
    if price > a:
        print("B " + str(price))
        break
    
    price += 1000
    if price > b:
        print("A " + str(price))
        break