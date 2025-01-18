class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price, quantity, discount=10):
        if item in self.cart:
            self.cart[item]['quantity'] += quantity
        elif item in self.cart:
            self.cart[item]['discount'] = discount
        else:
            self.cart[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]
        else:
            print(f"Item {item} not found in the cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            for item, details in self.cart.items():
                print(f"{item}: ${details['price']} x {details['quantity']}")

    def checkout(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        print(f"Total amount: ${total:.2f}")
        self.cart.clear()

def main():
    cart = ShoppingCart()
    while True:
        print("\nOptions: add, remove, view, checkout, quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'add':
            item = input("Enter item name: ").strip()
            price = float(input("Enter item price: ").strip())
            quantity = int(input("Enter item quantity: ").strip())
            discount = int(input("enter discount:").strip())
            cart.add_item(item, price, quantity)
        elif choice == 'remove':
            item = input("Enter item name to remove: ").strip()
            cart.remove_item(item)
        elif choice == 'view':
            cart.view_cart()
        elif choice == 'checkout':
            cart.checkout()
        elif choice == 'quit':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()