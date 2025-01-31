# Sales Tracking System

Your group is tasksed with building a Sales Tracking System for a small retail business. The business sells a variety of products and needs a system to manage inventory, track sales, calculate revenue, and analyze sales performance. The system should be simple, interactive, and easy to use.

The business currently uses manual methods to track sales and inventory, which is time-consuming and prone to errors. They need a digital solution that can:

1. Add new products to the inventory.
2. Record sales and update inventory in real-time.
3. Display the current inventory.
4. Calculate total revenue from all sales.
5. Analyze sales performance to identify the best-selling product.

Your team is tasked with building a Python program that simulates the Real-Time Sales Tracking System. The program should allow users to interact with the system dynamically (e.g., add products, record sales, view inventory) and provide real-time updates on inventory, revenue, and sales performance.

## Key Features

1. **Add Product**

    - Allow users to add a new product with a unique product ID, name, price, and quantity.

2. **Record Sale**

    - Allow users to record a sale by specifying the product ID and quantity sold.
    - Update the product's quantity in stock and store the sale details.

3. **View Inventory**

    - Display the current inventory (i.e., all products and their quantities).

4. **Calculate Total Revenue**

    - Calculate and display the total revenue from all recorded sales.

5. **Analyze Sales Performance**

    - Display the best-selling product (i.e., the product with the highest total sales quantity).

6. **Dynamic Interaction**

    - Instead of a static menu, the app will prompt the user for actions dynamically (e.g., "What would you like to do next?").

7. **Error Handling**

    - Handle invalid inputs (e.g., non-numeric values for product ID or quantity) and display user-friendly error messages.

8. **Modularize**

    - Divide the program into functions to handle different operations.
    - Every function should have a clear purpose and return values as needed, and they should be separated from the main program logic.

## Interaction

```codeowners title="Example"
Welcome to the Real-Time Sales Tracking System!

What would you like to do? (add/record/view/revenue/analyze/exit): add
Enter product ID: 101
Enter product name: Laptop
Enter product price: 1200
Enter product quantity: 10
Product added successfully!

What would you like to do? (add/record/view/revenue/analyze/exit): record
Enter product ID: 101
Enter quantity sold: 2
Sale recorded successfully!

What would you like to do? (add/record/view/revenue/analyze/exit): view
Current Inventory:
- Laptop (ID: 101): 8 in stock

What would you like to do? (add/record/view/revenue/analyze/exit): revenue
Total Revenue: $2400.0

What would you like to do? (add/record/view/revenue/analyze/exit): analyze
Best-Selling Product: Laptop (ID: 101) - 2 sold

What would you like to do? (add/record/view/revenue/analyze/exit): exit
Thank you for using the Real-Time Sales Tracking System!
```
