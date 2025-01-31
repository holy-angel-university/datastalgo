from data import products

def view_inventory():
    if not products:
        print("No products found.")
    else:
        print("Current Inventory:")
        for product_id, details in products.items():
            print(f"- {details['name']} (ID: {product_id}): {details['quantity']} in stock")
