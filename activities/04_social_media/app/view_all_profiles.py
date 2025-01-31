from users import users

def view_all_profiles():
    try:
        if not users:
            print("No profiles found.")
        else:
            print("All Profiles:")
            for i, (username, details) in enumerate(users.items(), 1):
                print(f"{i}. {details['name']} ({username})")
    except Exception as e:
        print(f"An error occurred: {e}")
