import random


class Dog:
    """Simple attempt to model a dog"""

    def __init__(self, name: str, age: int):
        """Initialize age and name attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(f"{self.name} is now sitting")

    def rollover(self):
        """Simulate a dog sitting"""
        print(f"{self.name} rolled over")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.rollover()


class Car:
    """Simple attempt to model a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing mileage"""
        print(f"The car has {self.odometer} miles on it")

    def update_odometer(self, mileage):
        """Set the odometer to a given value.
        reject the change if it tries to roll the odometer back
        """
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to th odometer reading"""
        self.odometer += miles


my_car = Car('audi', 'a4', 2024)
print(my_car.descriptive_name())
my_car.read_odometer()
my_car.odometer = 70
my_car.read_odometer()

my_car.update_odometer(23)
my_car.read_odometer()

my_car.increment_odometer(50)
my_car.read_odometer()


# Inheritance
class ElectricCar(Car):
    """Initializes attributes of parent class
    Then initializes attributes specific to an electric car"""

    def __init__(self, make, model, year):
        # Initialize attributes of parent class
        super().__init__(make, model, year)

        # Attribute specific to ElectricCar
        self.battery = Battery()  # Calling attributes of battery class into electric car

    def fill_gas_tank(self):
        """Electric Cars don't have a gas tank"""
        print(f"{self.descriptive_name()} doesn't need a gas tank.")


class Battery:
    def __init__(self, battery_size=75):
        """Initializes the battery attributes"""
        self.battery_size = battery_size
        self.ranges = 0

    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            self.ranges = 260
        elif self.battery_size == 150:
            self.ranges = 315

        print(f"This car can go about {self.ranges} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 150
        else:
            print(f"{self.battery_size} is already greater than or equal to 100")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


class Restaurant:
    """A simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type arguments"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Describes that the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is open")


class IceCreamStand(Restaurant):
    """Simple attempt to model an ice cream stand, a type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type, flavours=None):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def display_flavour(self):
        for flavour in self.flavours:
            print(flavour)


my_icecream_stand = IceCreamStand("Nana's Ice Cream", 'Ice Cream', ['chocolate', 'banana'])
my_icecream_stand.display_flavour()

#  JUST LIKE FUNCTIONS YOU CAN IMPORT CLASSES FROM OTHER FILES THE SAME WAY IT IS DONE DURING FUNCTIONS

# Python Standard library


class Die:
    """A simple attempt to model a die"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


my_die = Die()

for x in range(10):
    my_die.roll_die()


my_list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9]
for y in range(4):
    print(f"The winner is {random.choice(my_list)}")

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = random.choice(values)

for i in range(0, len(values)):
    print(random.choice(values))
    if values[i] == my_ticket:
        print(f"It took {i + 1} iterations to get the ticket {values[i]}")
        break

