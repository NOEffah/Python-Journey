# Greeting user
import json


def get_username():
    filename = "user_name.json"
    try:
        with open(filename, 'r') as fileobject:
            user1 = json.load(fileobject)
    except FileNotFoundError:
        create_new_user()
    else:
        return user1


def create_new_user():
    filename = "user_name.json"
    print("Sorry username cannot be found!\nSign up instead: ")
    user1 = input("Enter your name: ")
    with open(filename, 'w') as fileobject:
        json.dump(user1, fileobject)
        print(f"We will remember you when you come back {user1}.")


def greet_user():
    user0 = input("Enter your name: ")
    user1 = get_username()
    if user0 == user1:
        print(f"Welcome back, {user0.title()}")
    else:
        create_new_user()


greet_user()
