# Super Market Billing System

## Scenario

You are tasked with creating a simple supermarket billing system. The system should allow the cashier to input the items purchased by a customer, calculate the total bill, apply discounts, and display the final amount to be paid.

## Requirements

1. **Item Input**
    - The cashier should be able to input the name, quantity, and price of each item.
    - The system should store these items in a list of dictionaries.
2. **Calculate Total Bill**
    - The system should calculate the total bill by summing up the cost of all items ($quantity * price$).
3. **Apply Discounts**
    - If the total bill is greater than $\$100$, apply a $10\%%$ discount.
    - If the total bill is greater than $\$200$, apply a $20\%$ discount.
4. **Display Final Bill**
    - The system should display the final bill amount after applying any discounts.
5. **Additional Features**
    - The system should ask the cashier if they want to add more items after each item is added.
    - The system should handle invalid inputs (e.g., negative quantities or prices).

## Example Output

Here is an example of the system's output:

```
Enter item name: Apple
Enter quantity: 5
Enter price per item: 1.5
Do you want to add more items? (yes/no): yes

Enter item name: Bread
Enter quantity: 2
Enter price per item: 3.0
Do you want to add more items? (yes/no): no

Total Bill: $13.5
Discount Applied: 10%
Final Amount to be Paid: $12.15
```

## Your Task

Write a Python program that implements the above scenario. Your code should include:

- Variables and data types
- Conditionals (if-else)
- Loops (while or for)
- Type casting (e.g., converting strings to floats)

## Hints

- Use a `while` loop to allow the cashier to add multiple items.
- Use a list of dictionaries to store the items.
- Use `if-else` statements to apply discounts.
- Use `float()` to handle prices and totals.

## Grading Criteria

- **Correctness (50%)**: Does the code work as expected? Does it handle invalid inputs?
- **Code Structure (30%)**: Is the code well-organized and easy to read?
- **Efficiency (20%)**: Does the code use loops and conditionals effectively?