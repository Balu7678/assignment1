class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty, price):
        item = [item_name, qty, price]
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    
    def total_amount(self):
        amount = 0
        for item in self.items:
            amount += item[2]
        return amount



cart = ShoppingCart()

cart.add_item("Papaya", 1,10)
cart.add_item("Guava", 2,5)
cart.add_item("Orange", 1,7)

print("Current Items in Cart:")
for item in cart.items:
    print("item name:", item[0], "  qty:", item[1],"  price:",item[2])


print("Total Quantity:", cart.calculate_total())
print("Total Amount:", cart.total_amount())

cart.remove_item("Orange")

print("\nUpdated Items in Cart after removing item:")
for item in cart.items:
    print("item name:", item[0], "  qty:", item[1],"  price:",item[2])


print("Total Quantity:", cart.calculate_total())
print("Total Amount:", cart.total_amount())
