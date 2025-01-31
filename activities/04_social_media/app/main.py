from create_profile import create_profile
from post_update import post_update
from view_feed import view_feed
from view_all_profiles import view_all_profiles

def main():
    while True:
        print("\nWelcome to the Social Media App!")
        print("1. Create Profile")
        print("2. Post Update")
        print("3. View My Feed")
        print("4. View All Profiles")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()
            if not choice:
                print("No input detected. Please enter a valid choice.")
                continue

            choice = int(choice)
            if choice == 1:
                create_profile()
            elif choice == 2:
                post_update()
            elif choice == 3:
                view_feed()
            elif choice == 4:
                view_all_profiles()
            elif choice == 5:
                print("Thank you for using the Social Media App!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the choice.")

if __name__ == "__main__":
    main()
