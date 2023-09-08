# USER INPUT
# message = input("Tell me something and I will repeat it back to you: ")
# print(message)

# prompt = "Tell me something and I will repeat it back to you: "
# prompt += "\nWhat is your name: "

# name = input(prompt)
# age = int(input("What is your age? "))
# print(age)
# if age >= 18:
#     print("He is old")

# height = int(input("How tall are you in inches? "))
# if height >= 48:
#     print("\nYou are tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you are a little older.")

# number = int(input("Enter a number and I will tell you if it even or old: "))

# if number % 2 == 0:
#     print(f"The number {number} is even.")
# else:
#     print(f"The number {number} is odd.")

# rental_car = input("What kind of rental car would you want: ")
# print(f"Let me see if I can find a {rental_car}.")

# rest_seat = int(input("How many people are in your seating: "))
# if rest_seat > 8:
#    print("Please wait for a table.")

# num = int(input("Kindly enter a number: "))
# if num % 10 == 0:
#     print(f"{num} is a multiple of 10")
# else:
#     print(f"{num} is not a multiple of 10")

# WHILE LOOP
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program: "

# active = True

# while active:
#     message = input(prompt)

#     if message.lower() == 'quit':
#         active = False
#     else:
#         print(message)

# USING BREAK
# while True:
#    city = input(prompt)

#    if city == 'quit':
#        break
#    else:
#       print(f"I'd love to go to {city.title()}")

# USING CONTINUE
current_nu = 0
while current_nu < 10:
    current_nu += 1
    if current_nu % 2 == 0:
        continue  # This skips the current value for the check of the while loop
    # It skips the rest of the while loop
    print(current_nu)

# TRY
active = True

while active:
    topping = input("\nWhat pizza topping would you like.\nType 'quit' to stop adding toppings: ")

    if topping != 'quit':
        print(f"You are adding {topping} to the pizza.")
    else:
        active = False

prompt = "Which pizza topping would you like to add?"
prompt += "\n(Type 'quit' to stop adding toppings): "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza")

entry = ("\nWELCOME TO THE THEATER\n"
         "1. Under 3 - Free\n"
         "2. Between 3 & 12 - $10\n"
         "3. Over 12 - $15")

while True:
    print(entry)
    age = input("How old are you: ")

    if age.lower() == 'quit':
        break
    else:
        age = int(input(age))
        if age < 3:
            price = 0
        elif age < 13:
            price = 10
        else:
            price = 15
        print(f"The ticket price is ${price}.")

# WHILE LOOPS WITH LISTS AND DICTIONARIES

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying {current_user.title()}.")
    confirmed_users.append(current_user)

print("\nThe following users have been verified:")
for user in confirmed_users:
    print(f"{user.title()}")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name: ")
    response = input("What is your say on the issue: ")

    responses[name] = response

    repeat = input("Would you like to let another person respond: (y/n)")

    if repeat.lower() == "y":
        polling_active = False

print("---Polling results---")
for key, value in responses.items():
    print(key.title())
    print(value)
    print("\n")

