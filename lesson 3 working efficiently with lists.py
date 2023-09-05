# for loop through lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick.")
    print(f"I can't wait to see your next trick {magician.title()}.\n")

print("Thank you everyone that was a great show.\n")

pizzas = ['pepperoni', 'meat', 'fish']
for pizza in pizzas:
    print(f"I like {pizza.title()}  pizza")
print("I really love pizza\n")

# using range function
for value in range(1, 6):
    print(value)

# changing range numbers to a list  of numbers
numbers = list(range(1, 5))

even_numbs = list(range(2, 11, 2))
print(even_numbs)

squares = []
for val in range(1, 11):
    square = val ** 2
    squares.append(square)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# try
twenty = list(range(2, 21, 2))
print(twenty)

million = list(range(1, 1000001))
# print(million)
print(min(million))
print(max(million))
print(sum(million))

odds = []
for odd in range(1, 20, 2):
    odds.append(odd)
print(odds)

threes = []
for three in range(3, 31, 3):
    threes.append(three)
print(threes)

cubs = []
for x in range(1, 11):
    cub = x ** 3
    cubs.append(cub)
print(cubs)


cubed = [cube ** 3 for cube in range(1, 11)]
print(cubed)

# working with part of a list (slice)
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'kokonte', 'carrot cake']
friend_foods = my_foods[:]  # if you did friend_foods = my_foods without the slicing both variables will share elements
my_foods.append('ice cream')
friend_foods.append('fufu')

print('My favourite foods are:')
print(my_foods)
print('\nMy friends favourite foods are:')
print(friend_foods)

animals = ['dog', 'cat', 'bird', 'mouse', 'horse']
print('The first three items of the list are:')
for a in animals[:3]:
    print(a.title())

print('\nThree items from the middle of the list are:')
for b in animals[1:4]:
    print(b.title())

print('\nThree last three items from the list are:')
for c in animals[2:]:
    print(c.title())

pizza = ['pepperoni', 'cheese', 'margarita']
friend_pizza = pizza[:]

pizza.append('french')
friend_pizza.append('hawaiian')

print('\nPizza items:')
for d in pizza:
    print(d)

print('\nFriend Pizza items:')
for e in friend_pizza:
    print(e)

# TUPLES - used when elements are not to be changed
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:  # you can iterate through tuples though
    print(dimension)

fuds = ('pizza', 'burger', 'pasta', 'rice', 'bread')
for f in fuds:
    print(f)
