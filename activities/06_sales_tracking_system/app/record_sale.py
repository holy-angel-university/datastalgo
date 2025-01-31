from data import products, sales

def record_sale():
    try:
        product_id = int(input("Enter product ID: "))
        if product_id not in products:
            print("Product not found. Please check the product ID.")
            return

        quantity_sold = int(input("Enter quantity sold: "))
        if quantity_sold > products[product_id]["quantity"]:
            print("Insufficient stock. Please check the quantity.")
            return

        # Update product quantity
        products[product_id]["quantity"] -= quantity_sold

        # Record sale
        sale_price = products[product_id]["price"] * quantity_sold
        sales.append({"product_id": product_id, "quantity_sold": quantity_sold, "sale_price": sale_price})
        print("Sale recorded successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and quantity.")
