from data import sales

def calculate_revenue():
    total_revenue = sum(sale["sale_price"] for sale in sales)
    print(f"Total Revenue: ${total_revenue:.2f}")
