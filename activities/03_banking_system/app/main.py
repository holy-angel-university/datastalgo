# main.py
from create_account import create_account
from deposit import deposit
from withdraw import withdraw
from check_balance import check_balance


# Main program loop
def main():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_account()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                check_balance()
            elif choice == 5:
                print("Thank you for using the Banking System!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the choice.")


# Run the program
if __name__ == "__main__":
    main()
