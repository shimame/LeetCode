class SuperCar:
    def __init__(self, fuel, efficient):
        self.fuel = fuel
        self.efficient = efficient
        self.sum_distance = 0

    def run(self):
        if self.fuel != 0:
            self.fuel -= 1
            self.sum_distance += self.efficient
class SuperSuperCar(SuperCar):
    def fly(self):
        if self.fuel >= 5:
            self.fuel -= 5
            self.sum_distance += self.efficient ** 2
        else:
            self.run()
class SuperSuperSuperCar(SuperSuperCar):
    def fly(self):
        if self.fuel >= 5:
            self.fuel -= 5
            self.sum_distance += 2 * self.efficient ** 2
        else:
            self.run()
    def teleport(self):
        if self.fuel >= self.efficient ** 2:
            self.fuel -= self.efficient ** 2
            self.sum_distance += self.efficient ** 4
        else:
            self.fly()

N, K = [int(x) for x in input().split()]
cars = []
for _ in range(N):
    input_line = input().split()
    car_type = input_line[0]
    car_fuel = int(input_line[1])
    car_efficient = int(input_line[2])
    if car_type == "supercar":
        car = SuperCar(car_fuel, car_efficient)
    elif car_type == "supersupercar":
        car = SuperSuperCar(car_fuel, car_efficient)
    elif car_type == "supersupersupercar":
        car = SuperSuperSuperCar(car_fuel, car_efficient)
    cars.append(car)

for _ in range(K):
    input_line = input().split()
    car_num = int(input_line[0]) - 1
    car_func = input_line[1]
    if car_func == "run":
        cars[car_num].run()
    elif car_func == "fly":
        cars[car_num].fly()
    elif car_func == "teleport":
        cars[car_num].teleport()
    #print(f"car_num = {car_num + 1}, car.fuel = {cars[car_num].fuel}, car.sum_distance = {cars[car_num].sum_distance}")
for i in cars:
    print(i.sum_distance)
