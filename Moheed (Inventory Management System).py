class Product:
    def __init__(self, product_id, name, quantity, unit_price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def display_product(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Unit Price: ${self.unit_price:.2f}\n")


class Order:
    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Product ID: {self.product_id}")
        print(f"Quantity: {self.quantity}")
        print("------------------------")


class ManufacturingInventorySystem:
    def __init__(self):
        self.products = {}
        self.orders = {}
        self.order_id_counter = 1

    def create_product(self):
        try:
            product_id = int(input("Enter new product ID: "))
            if product_id in self.products:
                print("Error: Product ID already exists.\n")
                return
            
            name = input("Enter product name: ")
            quantity = int(input("Enter initial quantity: "))
            unit_price = float(input("Enter unit price: "))
            
            product = Product(product_id, name, quantity, unit_price)
            self.products[product_id] = product
            print(f"\nProduct '{name}' created successfully with ID {product_id}.\n")
        except ValueError:
            print("Invalid input. Please enter correct data types.\n")

    def read_product(self):
        try:
            product_id = int(input("Enter product ID to view details: "))
            product = self.products.get(product_id)
            if product:
                print("\nProduct Details:")
                product.display_product()
            else:
                print("Product not found.\n")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.\n")

    def update_product(self):
        try:
            product_id = int(input("Enter product ID to update: "))
            product = self.products.get(product_id)
            if product:
                name = input("Enter new name (press Enter to skip): ")
                quantity = input("Enter new quantity (press Enter to skip): ")
                unit_price = input("Enter new unit price (press Enter to skip): ")
                if name:
                    product.name = name
                if quantity:
                    product.quantity = int(quantity)
                if unit_price:
                    product.unit_price = float(unit_price)
                print(f"Product with ID {product_id} updated successfully.\n")
            else:
                print("Product not found.\n")
        except ValueError:
            print("Invalid input. Please enter correct data types.\n")

    def delete_product(self):
        try:
            product_id = int(input("Enter product ID to delete: "))
            if self.products.pop(product_id, None):
                print(f"Product with ID {product_id} deleted successfully.\n")
            else:
                print("Product not found.\n")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.\n")

    def place_order(self):
        try:
            product_id = int(input("Enter product ID to place an order for: "))
            quantity = int(input("Enter order quantity: "))
            product = self.products.get(product_id)
            if product:
                if product.quantity >= quantity:
                    order_id = self.order_id_counter
                    order = Order(order_id, product_id, quantity)
                    self.orders[order_id] = order
                    product.quantity -= quantity
                    self.order_id_counter += 1
                    print(f"Order {order_id} placed successfully for Product ID {product_id}.\n")
                else:
                    print("Insufficient quantity in stock.\n")
            else:
                print("Product not found.\n")
        except ValueError:
            print("Invalid input. Please enter correct data types.\n")

    def view_orders(self):
        if self.orders:
            print("\nOrder Details:")
            for order in self.orders.values():
                order.display_order()
        else:
            print("No orders have been placed.\n")


def display_banner():
    print("\n" + "="*30)
    print("         (PIAIC)")
    print("="*30 + "\n")


def main_menu():
    print("Manufacturing Inventory System Menu:")
    print("1. Create Product")
    print("2. Read Product Details")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Place Order")
    print("6. View Orders")
    print("7. Exit")


def main():
    system = ManufacturingInventorySystem()
    
    while True:
        display_banner()
        main_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            system.create_product()

        elif choice == "2":
            system.read_product()

        elif choice == "3":
            system.update_product()

        elif choice == "4":
            system.delete_product()

        elif choice == "5":
            system.place_order()

        elif choice == "6":
            system.view_orders()

        elif choice == "7":
            print("Exiting the Manufacturing Inventory System. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option from the menu.\n")


if __name__ == "__main__":
    main()
