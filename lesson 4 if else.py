cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'toyota':
        print(car.upper())
    else:
        print(car.title())

cer = 'bmw'  # for assignment
print(cer == 'bmw')  # for equality

print(cer == 'audi')
print(cer == 'Bmw')

requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print('Hold the Anchovies')

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("This is not the right answer")

ages = 21
print(ages < 21)
print(ages <= 21)

print(ages > 21)
print(ages >= 21)

age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('apple' in requested_toppings)

banned_users = ['andrew', 'caroline', 'david']

user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

car = 'subaru'
print("\nIs car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

aged = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet")
else:  # if age is lesser than 18 this executes
    print("Sorry you are too young to vote!")
    print("Please register to vot when you are 18 or older")

cade = 67

if cade < 4:
    price = 0
elif cade < 18:
    price = 25
elif cade < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is {price}. ")

# NOTE when you use elif only one conditions statements will be executed
# but when you use if differently all the cases you want to check will be executed
# you can use a for loop to prevent this though

alien_colors = ['green', 'yellow', 'red']
user_color = 'green'

if user_color in alien_colors:
    print("You have gained 5 points")

# using if statements with lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green pepper right now")
    else:
        print(f"Adding {requested_topping.title()}")
print("Finished making your pizza")

requested_toppings = []  # checking if a list is empty
if requested_toppings:  # will evaluate false if the list is empty and true if it is not
    print('kofi')

available_toppings = ['mushrooms', 'olives', 'green pepper', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}.")
    else:
        print(f"Sorry we dont have {requested_topping.title()} at the moment")

usernames = ['john', 'kel', 'seth', 'steve', 'admin']
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like a status report")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users")

