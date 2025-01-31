from collections import defaultdict
from data import products, sales

def analyze_performance():
    if not sales:
        print("No sales recorded yet.")
        return

    # Find the best-selling product
    sales_by_product = defaultdict(int)

    for sale in sales:
        sales_by_product[sale["product_id"]] += sale["quantity_sold"]

    best_product_id = max(sales_by_product, key=sales_by_product.get)
    best_product_name = products[best_product_id]["name"]
    best_quantity_sold = sales_by_product[best_product_id]

    print(f"Best-Selling Product: {best_product_name} (ID: {best_product_id}) - {best_quantity_sold} sold")
