from users import users

def create_profile():
    try:
        username = input("Enter your username: ")
        if username in users:
            print("Username already exists. Please choose a different username.")
            return

        name = input("Enter your name: ")
        users[username] = {"name": name, "posts": []}
        print("Profile created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
