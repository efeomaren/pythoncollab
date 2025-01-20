class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, **kwargs):
        item = {'name': name, 'price': price}
        item.update(kwargs)
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]

    def get_total(self):
        return sum(item['price'] for item in self.items)

    def list_items(self):
        return self.items

    def list_discounts(self):
        for item in self.items:
            if 'discount' in item:
                print(f"Item {item['name']} has a discount of {item['discount']}")
            else:
                print(f"Item {item['name']} does not have a discount")

def main():
    cart = ShoppingCart()
    
    actions = {
        'add': add_item_to_cart,
        'remove': remove_item_from_cart,
        'list': list_items_in_cart,
        'total': show_total_price,
        'discounts': list_item_discounts,
        'quit': quit_program
    }
    
    while True:
        action = input("Enter action (add, remove, list, total, discounts, quit): ").strip().lower()
        if action in actions:
            actions[action](cart)
        else:
            print("Invalid action. Please try again.")

def add_item_to_cart(cart):
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: ").strip())
    quantity = int(input("Enter item quantity: ").strip())
    category = input("Enter item category: ").strip()
    weight = float(input("Enter item weight: ").strip())
    size = input("Enter item size: ").strip()
    discount = float(input("Enter item discount: ").strip())
    cart.add_item(name, price, quantity=quantity, category=category, weight=weight, size=size, discount=discount)

def remove_item_from_cart(cart):
    name = input("Enter item name to remove: ").strip()
    cart.remove_item(name)

def list_items_in_cart(cart):
    print("Items in cart:", cart.list_items())

def show_total_price(cart):
    print("Total price:", cart.get_total())

def list_item_discounts(cart):
    cart.list_discounts()

def quit_program(cart):
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main()