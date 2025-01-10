# Super Market Billing System

## Scenario

You are tasked with creating a simple supermarket billing system. The system should allow the cashier to input the items purchased by a customer, calculate the total bill, apply discounts, and display the final amount to be paid.

## Requirements

1. The cashier should be able to input the name, quantity, and price of each item. The system should store these items in a list of dictionaries.
2. The system should calculate the total bill by summing up the cost of all items (`quantity * price`).
3. If the total bill is greater than 100, apply a 1% discount then if the total bill is greater than 200, apply a 2% discount and so on... it should be incremental by 1% for every 100 increment in the total bill.
4. The system should display the final bill amount after applying any discounts.
5. The system should ask the cashier if they want to add more items after each item is added and system should handle invalid inputs (e.g., negative quantities or prices).

## Example Output

Here is an example of the system's output:

```plaintext
Enter item name: Banana
Enter quantity: e
ERROR! Quantity must be a valid integer.
Enter quantity: -5
ERROR! Quantity must be a positive integer.
Enter quantity: 10
Enter price per item: $abc
ERROR! Price must be a valid number.
Enter price per item: $-2
ERROR! Price must be a positive number.
Enter price per item: $0.5
Do you want to add more items? (yes/no): maybe
ERROR! Please enter 'yes' or 'no'.
Do you want to add more items? (yes/no): no

Total Bill: $5.00
Discount Applied: 0%
Final Amount to be Paid: $5.00
```

## Hints

- Use a `while` loop to allow the cashier to add multiple items.
- Use a list of dictionaries to store the items.
- Use `if-else` statements to apply discounts.
- Use `float()` to handle prices and totals.