class Shop:
    def __init__(self):
        self.balance = 0
        self.sections = {
            'Electronics': {'Laptop': 1000, 'Smartphone': 800, 'Headphones': 150},
            'Clothing': {'Shirt': 50, 'Jeans': 80, 'Jacket': 120},
            'Groceries': {'Milk': 3, 'Bread': 2, 'Eggs': 5}
        }

    def add_balance(self, amount):
        self.balance += amount
        print(f"Balance successfully updated. Current balance: ${self.balance}")

    def show_balance(self):
        print(f"Current balance: ${self.balance}")

    def show_sections(self):
        print("Available sections:")
        for section in self.sections:
            print(section)

    def show_items(self, section):
        if section in self.sections:
            print(f"Items in {section}:")
            for item, price in self.sections[section].items():
                print(f"{item}: ${price}")
        else:
            print("Invalid section. Please choose a valid section.")

    def purchase_item(self, section, item):
        if section in self.sections and item in self.sections[section]:
            price = self.sections[section][item]
            if self.balance >= price:
                self.balance -= price
                print(f"{item} purchased successfully for ${price}. Remaining balance: ${self.balance}")
            else:
                print(f"Insufficient balance to purchase {item}.")
        else:
            print("Invalid section or item. Please choose a valid section and item.")

def main():
    shop = Shop()
    while True:
        print("\n1. Add Balance")
        print("2. Show Balance")
        print("3. Show Sections")
        print("4. Show Items")
        print("5. Purchase Item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter the amount to add to your balance: "))
            shop.add_balance(amount)
        elif choice == '2':
            shop.show_balance()
        elif choice == '3':
            shop.show_sections()
        elif choice == '4':
            section = input("Enter the section name: ")
            shop.show_items(section)
        elif choice == '5':
            section = input("Enter the section name: ")
            item = input("Enter the item name: ")
            shop.purchase_item(section, item)
        elif choice == '6':
            print("Exiting the shop. Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()