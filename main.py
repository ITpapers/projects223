class Car:
    amount_of_cars = 0
    def __init__(self, brand="Mers", cost=50):
        self.cost = cost
        self.total_value = cost*1000
        self.color = "Blue"
        self.brand = brand
        Car.amount_of_cars += 1

    def __str__(self):
        return f"{self.brand} is ${self.cost}/per day"

    def __del__(self):
        print( f"{self.brand} sold")


    def rent_out(self):
        self.total_value = self.total_value - (self.cost * 0.1)
        print(f"{self.brand} rented out!")




first_car = Car()

second_car = Car("Toyota", 35)


print(first_car)
