
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name}- ${self.price}"

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item:MenuItem):
        self.items.append(item)

    def display_menu(self):
        print("\n-----Menu-----")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item.get_details()}")

class Order:
    def __int__(self):
        self.ordered_items = []

    def add_to_ordered(self, item:MenuItem):
        self.ordered_items.append(item)
        print(f"added {item.name} to your order.")

    def get_total(self):
        return sum(item.price for item in self.ordered_items)

    def show_order(self):
        print("\n----your order------")

        for item in self.ordered_items:
            print(item.get_details())
        print(f"Total: ${self.get_total()}")

class Restaurant:
    restaurant_name  = "Guvi Food Hub"

    @staticmethod
    def welcome():
        print(f"Welcome to {Restaurant.restaurant_name}")

def main():
    Restaurant.welcome()

    menu = Menu()
    menu.add_item(MenuItem("Idli", 10))
    menu.add_item(MenuItem("Dosa", 20))
    menu.add_item(MenuItem("Pongal", 30))

    order = Order()

    menu.display_menu()

    while True:
        choice = input("Enter Item number to order or done to finish):")
        if choice.lower() == "done":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(menu.items):
            item = menu.items[int(choice)-1]
            order.add_to_ordered(item)
        else:
            print("invalid choice. try again")
    order.show_order()
    print("\n than you visit again")

if __name__== "__main__":
    main()
