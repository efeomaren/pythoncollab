class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, **kwargs):
        if 'discount' in kwargs and kwargs['discount'] > 0:
            print(f"Discount of {kwargs['discount']} applied to {name}")
        item = {'name': name, 'price': price}
        item.update(kwargs)
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]

    def get_total(self):
        return sum(item['price'] for item in self.items)

    def list_items(self):
        return self.items

if __name__ == "__main__":
    cart = ShoppingCart()
    
    while True:
        action = input("Enter action (add, remove, list, total, quit): ").strip().lower()
        
        if action == 'add':
            name = input("Enter item name: ").strip()
            price = float(input("Enter item price: ").strip())
            quantity = int(input("Enter item quantity: ").strip())
            category = input("Enter item category: ").strip()
            weight = float(input("Enter item weight: ").strip())
            size = input("Enter item size: ").strip()
            discount = float(input("Enter item discount: ").strip())
            cart.add_item(name, price, quantity=quantity, category=category, weight=weight, size=size, discount=discount)
        
        elif action == 'remove':
            name = input("Enter item name to remove: ").strip()
            cart.remove_item(name)
        
        elif action == 'list':
            print("Items in cart:", cart.list_items())
        
        elif action == 'total':
            print("Total price:", cart.get_total())
        
        elif action == 'quit':
            break
        
        else:
            print("Invalid action. Please try again.")