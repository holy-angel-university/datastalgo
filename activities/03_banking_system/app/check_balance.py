from create_account import accounts


def check_balance():
    try:
        account_number = int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account not found. Please check your account number.")
            return

        print(f"Your current balance is {accounts[account_number]['balance']}.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the account number.")
