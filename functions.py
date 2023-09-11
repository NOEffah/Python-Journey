def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")


def display():
    """This displays what we are learning in this lesson"""
    print("We are learning about functions")


# Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

# Default arguments
# Here you can set the argument while defining a function example. pet_name = 'dog'
# then when call the function you just define one argument example. describe_pet(animal_type='dog')


def make_shirt(size=10, text="I love Python"):
    """Prints a summary of the size and message about the text"""
    print(f"The size of the shirt is {size}")
    print(text)


def describe_city(city, country="Ghana"):
    print(f"{city.title()} is in {country.title()}")


# return values of statements
def get_formatted_name(first_name, last_name, middle_name=''):  # this makes the middle name optional
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


def build_person(first_names, last_names, age=None):
    """Return a directory of information about a person"""
    person = {'first': first_names, 'last': last_names}
    if age:
        person['age'] = age
    return person


def city_country(city_name, country):
    ret = f"{city_name.title()}, {country.title()}"
    return print(ret)


def make_album(artist_name, album_title, songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['songs'] = songs
    return print(album)


# Passing a list
def greet_users(names):
    """Print a greeting to user in a list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design until they are done"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all models that were created"""
    print(f"The following models have been printed")
    for model in completed_models:
        print(model)


def prints(mess):
    for messes in mess:
        print(messes)


def sending_message(unsent_msgs, sent_msgs):
    while unsent_msgs:
        current_msg = unsent_msgs.pop()
        print(f"Sending {current_msg}!")
        sent_msgs.append(current_msg)


def print_msg(sent_msgs):
    for sent_msg in sent_msgs:
        print(f"Printed messages: {sent_msg}")


# Passing an arbitrary number of arguments
def make_pizza(size, *toppings):  # *args is often when working with variable number of arguments
    """Summarize the pizza with the following toppings"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


def build_profile(first, last, **user_info):  # kwargs(key - word arguments)  default name for keyword arguments
    """Build a dictionary containing everything we know about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def sandwiches(*items):
    for item in items:
        print(f"Adding {item}")


def car(manufacture, model_name, **details):
    details['manu'] = manufacture
    details['model'] = model_name
    return details


