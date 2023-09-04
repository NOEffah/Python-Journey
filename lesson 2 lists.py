#declaring list items
bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle[0].title())
#printing items of a list
message = f"My first bicycle was {bicycle[-1].title()}."

print(message)
Friends = ['eva', 'adubea', 'dagadu', 'elsie', 'lesley']

friend_index = Friends[0]
print(f"Hello {friend_index.title()}.I have missed you.")
friend_index = Friends[1]
print(f"Hello {friend_index.title()}.I have missed you.")
friend_index = Friends[2]
print(f"Hello {friend_index.title()}.I have missed you.")
friend_index = Friends[3]
print(f"Hello {friend_index.title()}.I have missed you.")

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

# to replace list item
motocycles[0] = 'dubati'
print(motocycles)

# to add list element
motocycles.append('toyota')
print(motocycles)

# insert help to put the new element at a specific index
motocycles.insert(1, 'range')
print(motocycles)

# to remove a list item
# it removes only the first occurance of the value
motocycles.remove('range')
print(motocycles)

# to delete element index
del motocycles[0]
print(motocycles)

# to remove from a list and use for something else
# pop takes the last item by default if not specify eg.motocycle.pop(3)
popped_moto = motocycles.pop()
print(popped_moto)
print(motocycles)

# try work
guest_list = ['Elon Musk', 'Albert Einstein', 'Jeff Bezos']

print(f"Hello {guest_list[0]}, you are welcome for dinner")
print(f"Hello {guest_list[1]}, you are welcome for dinner")
print(f"Hello {guest_list[2]}, you are welcome for dinner")

print(f"{guest_list[0]} can't make it")

guest_list[0] = 'Thomas Edison'
print(f"Hello {guest_list[0]}, you are welcome for dinner")
print(f"Hello {guest_list[1]}, you are welcome for dinner")
print(f"Hello {guest_list[2]}, you are welcome for dinner")
print( )

guest_list.insert(0, 'Bright Effah')
guest_list.insert(2, 'Kofi Annan')
guest_list.append('Nicola Tesla')

print(f"Hello {guest_list[0]}, you are welcome for dinner")
print(f"Hello {guest_list[1]}, you are welcome for dinner")
print(f"Hello {guest_list[2]}, you are welcome for dinner")
print(f"Hello {guest_list[3]}, you are welcome for dinner")
print(f"Hello {guest_list[4]}, you are welcome for dinner")
print(f"Hello {guest_list[5]}, you are welcome for dinner")
print( )

current_pop = guest_list.pop()
print(f"{current_pop}, Sorry but you can no longer come")
current_pop = guest_list.pop()
print(f"{current_pop}, Sorry but you can no longer come")
current_pop = guest_list.pop()
print(f"{current_pop}, Sorry but you can no longer come")
current_pop = guest_list.pop()
print(f"{current_pop}, Sorry but you can no longer come")
print( )

print(f"Hello {guest_list[0]}, you are still welcome for dinner")
print(f"Hello {guest_list[1]}, you are still welcome for dinner")
print( )

del guest_list[1]
del guest_list[0]
print(guest_list)
