class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand}: {self.model}"
    

class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size


my_ev = ElectricCar("Tata", "Punch", "80kWh")

# print(my_ev.brand)
print(my_ev.get_brand())



# my_car = Car("Toyta", "Fortuner")
# my_new_car = Car("Tata", "Shiera")
# print(my_new_car.full_name())
# print(my_car.full_name())


