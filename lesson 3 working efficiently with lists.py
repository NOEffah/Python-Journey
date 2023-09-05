# for loop through lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick.")
    print(f"I can't wait to see your next trick {magician.title()}.\n")

print("Thank you everyone that was a great show.\n")

pizzas = ['pepparoni', 'meat', 'fish']
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


