from Item import Item  # the first Item represents the file while the second one is the class called item in it
from Keyboard import Keyboard

item1 = Keyboard('MyItem', 750, 6)

item1.apply_discount()
print(item1.price)


