class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def drive_to_location(self, location):
        print(f"Car {self.model} is drining to {location}")

car_honda = Car("silver","Honda")
print(car_honda)

car_subaru = Car("black","Subaru")
print(car_subaru)


class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number
        
    def drive_to_location(self, location):
        print(f"Bus {self.model} is drining to {location}")
    def test_bus(self):
        print(f"Bus test {self.model}")

bus_40 = Bus("yellow", "Mersedes Benz")
bus_40.drive_to_location("Bishkek")
print(bus_40.color)

vehicles = [bus_40, car_honda]
for v in vehicles:
    v.drive_to_location("Bishkek")