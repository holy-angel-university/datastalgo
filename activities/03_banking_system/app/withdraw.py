from create_account import accounts


def withdraw():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account not found. Please check your account number.")
            return

        amount = float(input("Enter amount to withdraw: "))
        if amount < 0:
            print("Withdrawal amount cannot be negative. Please try again.")
            return

        if accounts[account_number]["balance"] < amount:
            print("Insufficient balance. Please try again.")
            return

        accounts[account_number]["balance"] -= amount
        print(
            f"Withdrawal successful! Your new balance is {accounts[account_number]['balance']}."
        )
    except ValueError:
        print(
            "Invalid input. Please enter a numeric value for the account number or amount."
        )
