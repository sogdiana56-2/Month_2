class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.__fined = False
    def drive_to_location(self, location):
        print(f"Car {self.model} is drining to {location}")
    def _test_car(self):
        print(f"test car {self.model}")

car_honda = Car("silver","Honda")
# print(car_honda)
# car_honda._test_car()
print(car_honda)