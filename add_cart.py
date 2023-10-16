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

cart.add_item("tv", 1,10000)
cart.add_item("phone", 2,50000)
cart.add_item("watch", 1,700)

print("Current Items in Cart:")
for item in cart.items:
    print("item name:", item[0], "  qty:", item[1],"  price:",item[2])


print("Total Quantity:", cart.calculate_total())
print("Total Amount:", cart.total_amount())

cart.remove_item("watch")

print("\nUpdated Items in Cart after removing item:")
for item in cart.items:
    print("item name:", item[0], "  qty:", item[1],"  price:",item[2])


print("Total Quantity:", cart.calculate_total())
print("Total Amount:", cart.total_amount())
