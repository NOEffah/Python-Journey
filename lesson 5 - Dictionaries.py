alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

alien_1 = {}
alien_1['color'] = 'white'
alien_1['points'] = 10
alien_1['x_position'] = 25
alien_1['y_position'] = 0
alien_1['speed'] = 'medium'

print(f"The alien is {alien_1['color'].title()}.")

alien_1['color'] = 'yellow'
print(f"The alien is {alien_1['color'].title()}.")

if alien_1['speed'] == 'slow':
    x_increment = 1
    alien_1['x_position'] += x_increment
elif alien_1['speed'] == 'medium':
    x_increment = 2
    alien_1['x_position'] += x_increment
else:
    x_increment = 3
    alien_1['x_position'] += x_increment
print(f"New position: {alien_1['x_position']}")

# removing entry
print(alien_1)
del alien_1['speed']
print(alien_1)

favourite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'python',
    'phil': 'ruby'
}

language = favourite_lang['sarah'].title()
print(f"Sarah's favourite programming language is {language}")

print(favourite_lang['jen'].title())
print(favourite_lang.get('jenny'))  # to check if key exists
print(favourite_lang.get('jen'))

# try
person = {
    'firstname': 'peter',
    'lastname': 'parker',
    'age': 25,
    'city': 'New York'
}

print(person['firstname'])
print(person['lastname'])
print(person['age'])
print(person['city'])

fav_num = {
    'peter': 7,
    'bob': 3,
    'logan': 5,
    'john': 7,
    'lisa': 9
}

print(f"Peter's favourite number is {fav_num['peter']}.")
print(f"Bob's favourite number is {fav_num['bob']}.")
print(f"Logan's favourite number is {fav_num['logan']}.")
print(f"John's favourite number is {fav_num['john']}.")
print(f"Lisa's favourite number is {fav_num['lisa']}.\n")

Glossary = {
    'variable': 'Used for storing data types',
    'boolean': 'True or False',
    'loops': 'Sequence of events that keep on happening',
    'list': 'Stores elements in an orderly manner',
    'dictionary': 'Stores elements in any order'
}

print(f"Variables: {Glossary['variable']}\n")
print(f"Boolean: {Glossary['boolean']}\n")
print(f"Loops: {Glossary['loops']}\n")
print(f"List: {Glossary['list']}\n")
print(f"Dictionary: {Glossary['dictionary']}\n")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# looping through dictionaries
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for keys in user_0.keys():
    print(f"\n{keys.title()}")

for pers, lang in favourite_lang.items():
    print(f"\n{pers.title()}: {lang.title()}")

for pers in favourite_lang.keys():
    print(f"{pers.title()}")

friends = ['phil', 'sarah']

for name in favourite_lang.keys():
    print(f"Hello, {name.title()}.  ")
    if name in friends:
        language = favourite_lang[name].title()
        print(f"{name.title()} I see you love {language}")

for name in sorted(favourite_lang.keys()):
    print(f"{name.title()}, thank you for taking the pole ")

for language in favourite_lang.values():
    print(language.title())

for language in set(favourite_lang.values()):  # take note of the set and how it makes every value unique
    print(language.title())


for key, value in Glossary.items():
    print(f"{key.title()}: {value }\n")


rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtse': 'china'
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

print("\n")
for river in rivers.keys():
    print(river.title())
print("\n")
for country in rivers.values():
    print(country.title())
print("\n")

poll_takers = ['kofi', 'phil', 'quami', 'jen', 'edward']

for poll_taker in poll_takers:
    if poll_taker in favourite_lang.keys():
        print(f"Thank you {poll_taker.title()} for responding")
    else:
        print(f"{poll_taker.title()}, kindly take the poll")

# storing dictionaries in list
grand = [alien_1, alien_0, favourite_lang, fav_num]
for dic in grand:
    print(dic)

aliens = []
for alien_num in range(0, 30):
    new_alien = {'color': 'brown', 'points': 50, 'speed': 'high'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

# storing list in dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

for topping in pizza['toppings']:
    print(topping.title())

for key, values in pizza.items():
    print(f"{key.title()}: {values}")

# dictionary inside a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
print("\nKeys:")
for username in users.keys():
    print(username)
print("Values:")
for values in users.values():
    print(values)

print("Keys and Values")
for username, values in users.items():
    print(f"{username}")
    fullname = f"{values['first']} {values['last']}"
    location = values['location']

    print(f"Fullname: {fullname.title()}")
    print(f"Location: {location.title()}")

person_0 = {'first_name': 'peter', 'last_name': 'parker', 'age': 28, 'city': 'New York'}
person_1 = {'first_name': 'marie', 'last_name': 'curie', 'age': 20, 'city': 'Los Angeles'}
person_2 = {'first_name': 'albert', 'last_name': 'einstein', 'age': 70, 'city': 'Chicago'}

people = [person_0, person_1, person_2]
print("\n")

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")

    print(" ")

dog = {'name': 'peace', 'owner_name': 'kofi'}
cat = {'name': 'kitty', 'owner_name': 'ama'}
parrot = {'name': 'kasa', 'owner_name': 'fiifi'}

pets = [dog, cat, parrot]
for pet in pets:
    for x, y in pet.items():
        print(f"{x.title()}: {y.title()}")
    print(" ")

favourite_places = {
    'ama': ['dubai', 'korea', 'accra'],
    'kofi': ['tanzania', 'uruguay', 'zimbabwe'],
    'castro': ['congo', 'canada', 'ghana']
}
for person, places in favourite_places.items():
    print(f"{person}:")
    for place in places:
        print(f"\t{place.title()}")
    print("\n")

cities = {
    'accra': {'country': 'Ghana',
              'population': 678231,
              'fact': 'Money making City'},
    'vancouver': {'country': 'USA',
                  'population': 12978139,
                  'fact': 'Dream land'},
    'bermuda': {'country': 'Ghana',
                'population': 231,
                'fact': 'Mystery'},
}
print("\n")
for city, items in cities.items():
    print(f"{city.title()}")
    Items = f"Country: {items['country']}\nPopulation: {items['population']}\nFact: {items['fact']}"
    print(Items)
    print(" ")
