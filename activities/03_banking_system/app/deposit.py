from create_account import accounts


def deposit():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account not found. Please check your account number.")
            return

        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print("Deposit amount cannot be negative. Please try again.")
            return

        accounts[account_number]["balance"] += amount
        print(
            f"Deposit successful! Your new balance is {accounts[account_number]['balance']}."
        )
    except ValueError:
        print(
            "Invalid input. Please enter a numeric value for the account number or amount."
        )
