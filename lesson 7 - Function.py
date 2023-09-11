def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")


greet_user('jesse')


def display():
    """This displays what we are learning in this lesson"""
    print("We are learning about functions")


display()


# Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')  # positional arguments
describe_pet(animal_type='dog', pet_name='peace')  # key word arguments

# Default arguments
# Here you can set the argument while defining a function example. pet_name = 'dog'
# then when call the function you just define one argument example. describe_pet(animal_type='dog')


def make_shirt(size=10, text="I love Python"):
    """Prints a summary of the size and message about the text"""
    print(f"The size of the shirt is {size}")
    print(text)


make_shirt()


def describe_city(city, country="Ghana"):
    print(f"{city.title()} is in {country.title()}")


describe_city("Accra")
describe_city("Seattle")
describe_city("Tem")


# return values of statements
def get_formatted_name(first_name, last_name, middle_name=''):  # this makes the middle name optional
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at anytime to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")


def build_person(first_names, last_names, age=None):
    """Return a directory of information about a person"""
    person = {'first': first_names, 'last': last_names}
    if age:
        person['age'] = age
    return person


music = build_person('jimi', 'hendrix', age=27)
print(music)

musician = get_formatted_name('jimi', 'hendrix')
musician_name = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def city_country(city_name, country):
    ret = f"{city_name.title()}, {country.title()}"
    return print(ret)


city_country('accra', 'ghana')
city_country('lesotho', 'south africa')
city_country('dakar', 'senegal')


def make_album(artist_name, album_title, songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['songs'] = songs
    return print(album)


while True:
    print("\nMake an album:")
    print("(Enter 'q' anytime you want to quit)")
    art_name = input("Enter Artist Name: ")
    if art_name == 'q':
        break

    alb_name = input("Enter Album Name: ")
    if alb_name == 'q':
        break

    make_album(art_name, alb_name)


make_album('MOG', 'Grace unplugged')
make_album('Joe Mettle', 'Revival')
make_album('Nana Effah', 'All I want is You', 200)


# Passing a list
def greet_users(names):
    """Print a greeting to user in a list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', "ty", 'margot']
greet_users(usernames)


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


unprinted_designes = ['phone case', 'robot pendant', 'dodecahedron']
completed_modes = []

print_models(unprinted_designes[:], completed_modes)  # this helps pass a copy of the original list to the function
show_completed_models(completed_modes)

short_text = ['hi', 'hello', 'whatsup']
sent = []


def prints(mess):
    for messes in mess:
        print(messes)


prints(short_text)


def sending_message(unsent_msgs, sent_msgs):
    while unsent_msgs:
        current_msg = unsent_msgs.pop()
        print(f"Sending {current_msg}!")
        sent_msgs.append(current_msg)


def print_msg(sent_msgs):
    for sent_msg in sent_msgs:
        print(f"Printed messages: {sent_msg}")


sending_message(short_text[:], sent)
print_msg(sent)

print(short_text)
print(sent)


# Passing an arbitrary number of arguments
def make_pizza(size, *toppings):  # *args is often when working with variable number of arguments
    """Summarize the pizza with the following toppings"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):  # kwargs(key - word arguments)  default name for keyword arguments
    """Build a dictionary containing everything we know about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


def sandwiches(*items):
    for item in items:
        print(f"Adding {item}")


sandwiches()
sandwiches('methane', 'salt', 'cabbage')
sandwiches('bread', 'onion')


build_profile('Nana', 'Effah', location='Seattle', country='USA', religion='Christian')


def car(manufacture, model_name, **details):
    details['manu'] = manufacture
    details['model'] = model_name
    return details


car1 = car('subaru', 'outback', color='blue', tow_package=True)
print(car1)


# Storing functions in modules

