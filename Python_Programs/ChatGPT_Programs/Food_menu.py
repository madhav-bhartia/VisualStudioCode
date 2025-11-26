import csv


def print_menu(menu):
    print("\nMenu:")
    print("-" * 50)
    for item in menu:
        print(f"{item['item']:25} {item['price']:>5} INR")
    print("-" * 50)


def get_order(menu):
    order = []
    print("\nEnter your order (press enter when finished):")
    while True:
        choice = input().strip()
        if not choice:
            break
        found = False
        for item in menu:
            if choice.lower() == item["name"].lower():
                order.append(item)
                found = True
                break
        if not found:
            print(f"Sorry, '{choice}' is not on the menu. Please try again.")
    return order


def calculate_total(order):
    total = sum(item["price"] for item in order)
    return total


def main():
    # Load the menu from the CSV file
    with open(
        r"c:\VisualStudioCode\Python Programs\ChatGPT_Programs\menu.csv", "r"
    ) as f:
        reader = csv.DictReader(f)
        menu = list(reader)

    # Print the menu
    print_menu(menu)

    # Get the order
    order = get_order(menu)

    # Calculate the total
    total = calculate_total(order)

    # Print the total
    print(f"\nYour total is: {total} INR")


if __name__ == "__main__":
    main()
