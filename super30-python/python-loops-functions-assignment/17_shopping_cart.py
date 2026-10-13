# Q17. Shopping Cart using Functions:
# Create functions for add_item(), remove_item(), view_cart(), calculate_total(), and checkout().
# Keep the application running using a while loop until checkout or exit.

# Default item catalog: {item_name: price per unit in Rs.}
CATALOG = {
    "rice (1 kg)": 60,
    "wheat flour (1 kg)": 45,
    "sugar (1 kg)": 42,
    "milk (1 litre)": 28,
    "eggs (dozen)": 80,
    "bread": 35,
    "apple (1 kg)": 150,
    "banana (dozen)": 50,
    "tea powder (250 g)": 120,
    "cooking oil (1 litre)": 140,
}

# cart structure: {item_name: {"price": float, "qty": int}}


def view_catalog():
    print(f"\n{'No.':<5}{'Item':<24}{'Price (Rs.)':>12}")
    print("-" * 41)
    for number, (name, price) in enumerate(CATALOG.items(), start=1):
        print(f"{number:<5}{name:<24}{price:>12}")


def add_item(cart):
    view_catalog()
    item_names = list(CATALOG)
    choice = input("\nEnter item number (or name) to add : ").strip().lower()

    if choice.isdigit() and 1 <= int(choice) <= len(item_names):
        name = item_names[int(choice) - 1]
    elif choice in CATALOG:
        name = choice
    else:
        print("Item not found in the catalog.")
        return

    try:
        qty = int(input(f"Enter quantity of {name} : "))
    except ValueError:
        print("Invalid input. Quantity must be a whole number.")
        return
    if qty <= 0:
        print("Quantity must be greater than 0.")
        return

    price = CATALOG[name]
    if name in cart:
        cart[name]["qty"] += qty
    else:
        cart[name] = {"price": price, "qty": qty}
    print(f"Added {qty} x {name} @ Rs. {price}")


def remove_item(cart):
    if not cart:
        print("Your cart is empty.")
        return
    name = input("Enter item name to remove : ").strip().lower()
    if name in cart:
        del cart[name]
        print(f"Removed {name} from the cart.")
    else:
        print(f"'{name}' is not in the cart.")


def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    print(f"\n{'Item':<15}{'Price':>10}{'Qty':>6}{'Subtotal':>12}")
    print("-" * 43)
    for name, details in cart.items():
        subtotal = details["price"] * details["qty"]
        print(f"{name:<15}{details['price']:>10.2f}{details['qty']:>6}{subtotal:>12.2f}")


def calculate_total(cart):
    total = 0
    for details in cart.values():
        total += details["price"] * details["qty"]
    return total


def checkout(cart):
    if not cart:
        print("Your cart is empty. Add items before checkout.")
        return False
    print("\n===== Final Bill =====")
    view_cart(cart)
    print("-" * 43)
    print(f"{'Total':<31}{calculate_total(cart):>12.2f}")
    print("\nThank you for shopping with us!")
    return True


def shopping_cart():
    cart = {}
    while True:
        print()
        print("===== Shopping Cart =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Calculate Total")
        print("5. Checkout")
        print("6. Exit")

        try:
            choice = input("\nEnter your choice (1-6): ")
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            break

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            print(f"Cart total: Rs. {calculate_total(cart):.2f}")
        elif choice == "5":
            if checkout(cart):
                break
        elif choice == "6":
            print("Exiting without checkout. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    shopping_cart()
