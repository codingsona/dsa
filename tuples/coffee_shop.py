from typing import Tuple, NamedTuple

# Step1: let's create a class to represent one purchase
class Item(NamedTuple):
    id: int
    name: str
    price: int

# Step2: Lets initialize few items
coffee = Item(1, "Coffee", 100)
tea = Item(2, "Tea", 200)
biscuit = Item(3, "Biscuit", 50)

#print(f'Item: {coffee.name}, Price: {coffee.price}')
#coffee.price = 150


# Step3: To represent multiple items in a order, create a class Order
class Order(NamedTuple):
    order_id: int
    items: Tuple[Item]
    def total_price(self):
        return sum(item.price for item in self.items)


order1 = Order(1, (tea, biscuit))
#print(f'Total price of order1 is: {order1.total_price()}')


order2 = Order(2, (coffee, biscuit))
print(f'Total price of order2 is: {order2.total_price()}')

