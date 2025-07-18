def display_menu(menu):
    print("WELCOME TO RAJA STORES\n")
    print("MENU\n")

    sections = {
        "COSMETICS": range(1, 17),
        "FOOD ITEMS": range(1, 17),
        "HOME USAGE ITEMS": range(17, 33),
        "FOOD GROCERIES": range(17, 33),
        "DETERGENTS": range(33, 43)
    }

    # Cosmetics and Food Items
    print("COSMETICS:                           FOOD ITEMS:")
    for item_num in range(1, 17):
        if item_num in menu:
            item = menu[item_num]
            print(f"{item_num}. {item['name']} - {item['price']:.2f}\t\t", end='')
            if item_num % 2 == 0:
                print()  # Newline after every two items for formatting

    print("\nHOME USAGE ITEMS:                    FOOD GROCERIES:")
    for item_num in range(17, 33):
        if item_num in menu:
            item = menu[item_num]
            print(f"{item_num}. {item['name']} - {item['price']:.2f}\t\t", end='')
            if (item_num - 16) % 2 == 0:
                print()

    print("\nDETERGENTS:")
    for item_num in range(33, 43):
        if item_num in menu:
            item = menu[item_num]
            print(f"{item_num}. {item['name']} - {item['price']:.2f}")

    print("\n" + "-"*51)
    print("STORE OFFER - UP TO 5% Off On Every Ordered Item")
    print("-"*51 + "\n")


def take_order(menu):
    order = []
    try:
        n = int(input("Enter the number of items to order: "))
        for i in range(n):
            while True:
                try:
                    choice = int(input(f"Enter the item number - {i + 1}: "))
                    if choice in menu:
                        order.append(choice)
                        break
                    else:
                        print("Invalid item number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
    except ValueError:
        print("Invalid input. Please enter a valid number of items.")
    return order


def calculate_bill(order, menu):
    bill = 0.0
    for item_num in order:
        bill += menu[item_num]['price']
    return bill


def apply_discount(bill, discount_rate=0.05):
    discount = bill * discount_rate
    return bill - discount


def display_bill(bill):
    print(f"\nTotal Bill: {bill:.2f} rupees\n")


def main():
    # Define the menu with item numbers, names, and prices
    menu = {
        # Cosmetics
        1: {"name": "Lipstick", "price": 199.00},
        2: {"name": "Chips Packet", "price": 50.00},
        3: {"name": "Face Cream", "price": 249.50},
        4: {"name": "Biscuits Pack", "price": 30.00},
        5: {"name": "Shampoo", "price": 120.00},
        6: {"name": "Juice Bottle", "price": 99.00},
        7: {"name": "Kajal", "price": 70.00},
        8: {"name": "Soft Drinks (1L)", "price": 85.00},
        9: {"name": "Nail Polish", "price": 150.00},
        10: {"name": "Instant Noodles", "price": 20.00},
        11: {"name": "Hair Oil", "price": 110.00},
        12: {"name": "Chocolate Box", "price": 250.00},
        13: {"name": "Foundation", "price": 300.00},
        14: {"name": "Cookies Jar", "price": 120.00},
        15: {"name": "Perfume", "price": 500.00},
        16: {"name": "Popcorn Pack", "price": 45.00},
        # Home Usage Items and Food Groceries
        17: {"name": "Floor Cleaner", "price": 85.00},
        18: {"name": "Rice Bag (5kg)", "price": 400.00},
        19: {"name": "Dishwash Liquid", "price": 75.00},
        20: {"name": "Wheat Flour (1kg)", "price": 60.00},
        21: {"name": "Air Freshener", "price": 180.00},
        22: {"name": "Sugar (1kg)", "price": 50.00},
        23: {"name": "Toilet Brush", "price": 70.00},
        24: {"name": "Cooking Oil (1L)", "price": 200.00},
        25: {"name": "Garbage Bags", "price": 90.00},
        26: {"name": "Pulses (1kg)", "price": 120.00},
        27: {"name": "Mop Stick", "price": 300.00},
        28: {"name": "Salt (1kg)", "price": 25.00},
        29: {"name": "Laundry Basket", "price": 350.00},
        30: {"name": "Spices Pack", "price": 150.00},
        31: {"name": "Kitchen Towels", "price": 100.00},
        32: {"name": "Tea Pack (250g)", "price": 150.00},
        # Detergents
        33: {"name": "Laundry Detergent", "price": 200.00},
        34: {"name": "Fabric Softener", "price": 150.00},
        35: {"name": "Detergent Powder", "price": 90.00},
        36: {"name": "Toilet Cleaner", "price": 120.00},
        37: {"name": "Dishwash Bar", "price": 25.00},
        38: {"name": "Bleach", "price": 50.00},
        39: {"name": "Stain Remover", "price": 180.00},
        40: {"name": "Glass Cleaner", "price": 70.00},
        41: {"name": "Handwash Liquid", "price": 100.00},
        42: {"name": "Cleaning Gloves", "price": 90.00}
    }

    display_menu(menu)
    order = take_order(menu)
    if not order:
        print("No items ordered. Exiting.")
        return
    bill = calculate_bill(order, menu)
    bill_after_discount = apply_discount(bill)
    display_bill(bill_after_discount)


if __name__ == "__main__":
    main()