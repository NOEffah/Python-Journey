class Item:
    pay_rate = 0.8  # The pay rate after 20% discount This is a class attribute
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item('Phone', 100, 3)

item2 = Item('Laptop', 1000, 1)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
# print(Item.__dict__)
# print(item2.__dict__)

item1.apply_discount()
print(item1.price)

item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

print(Item.all)
for instance in Item.all:
    var = instance.name
    print(var)
