accounts = {}


def create_account():
    try:
        name = input("Enter your name: ")
        balance = float(input("Enter initial balance: "))
        if balance < 0:
            print("Initial balance cannot be negative. Please try again.")
            return

        # Generate a unique account number
        account_number = len(accounts) + 1001
        accounts[account_number] = {"name": name, "balance": balance}
        print(f"Account created successfully! Your account number is {account_number}.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the balance.")
