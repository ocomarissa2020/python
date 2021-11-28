class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

    def data(self):
        print(f"Car color is {self.color}, Model is {self.model}, Manufacture is {self.manufacturer}.")


car = Car("Red", "Everest", "Ford")
car1 = Car("Blue", "Fortuner", "Toyota")
car2 = Car("White", "mu-X", "Isuzu")
car3 = Car("Brown", "Terra", "Nissan")

car.data()
car1.data()
car2.data()
car3.data()
