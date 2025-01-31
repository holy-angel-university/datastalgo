# Banking System

Your group is tasked with building a Banking System App for a small bank. The app should allow users to interact with their bank accounts using a text-based menu. The system should handle multiple accounts and ensure that operations like withdrawals, deposits, and balance checks are performed correctly.

The bank currently uses manual methods to manage accounts, which is time-consuming and prone to errors. They need a digital solution that can:

1. Create new bank accounts with unique account numbers.
2. Allow users to deposit money into their accounts.
3. Allow users to withdraw money from their accounts.
4. Display the current balance of an account.
5. Handle errors gracefully, such as invalid inputs or insufficient funds.

Your team is tasked with building a Python program that simulates the Banking System App. The program should allow users to interact with the system dynamically (e.g., create accounts, deposit money, withdraw money) and provide real-time updates on account balances.

## Key Features

1. **Account Creation**

    - Allow users to create a new account with a unique account number, name, and initial balance.

2. **Deposit Money**

    - Allow users to deposit money into their account by specifying the account number and amount.
    - Update the account balance accordingly.

3. **Withdraw Money**

    - Allow users to withdraw money from their account by specifying the account number and amount.
    - Ensure the account has sufficient balance before allowing the withdrawal.

4. **Check Balance**

    - Allow users to check the current balance of their account by specifying the account number.

5. **Menu-Driven Interface**

    - Display a menu with options for creating accounts, depositing money, withdrawing money, checking balances, and exiting the program.

6. **Error Handling**

    - Handle invalid inputs (e.g., non-numeric values for amounts or account numbers) and display user-friendly error messages.

7. **Type Casting**

    - Convert user inputs (e.g., amounts) to appropriate data types (e.g., `float` for balance).

8. **Modularize**

    - Divide the program into functions to handle different operations.
    - Every function should have a clear purpose and return values as needed, and they should be separated from the main program logic.

## Interaction

```codeowners title="Example"
Welcome to the Banking System!
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit
Enter your choice: 1

Enter your name: John Doe
Enter initial balance: 1000
Account created successfully! Your account number is 12345.

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit
Enter your choice: 2

Enter your account number: 12345
Enter amount to deposit: 500
Deposit successful! Your new balance is 1500.0.

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit
Enter your choice: 4

Enter your account number: 12345
Your current balance is 1500.0.

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit
Enter your choice: 5

Thank you for using the Banking System!
```
