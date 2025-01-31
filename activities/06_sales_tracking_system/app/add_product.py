from data import products

def add_product():
    try:
        product_id = int(input("Enter product ID: "))
        if product_id in products:
            print("Product ID already exists. Please choose a different ID.")
            return

        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        products[product_id] = {"name": name, "price": price, "quantity": quantity}
        print("Product added successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for ID, price, and quantity.")
