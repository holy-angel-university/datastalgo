from users import users

def view_feed():
    try:
        username = input("Enter your username: ")
        if username not in users:
            print("User not found. Please check your username.")
            return

        posts = users[username]["posts"]
        if not posts:
            print("Your feed is empty.")
        else:
            print("Your Feed:")
            for i, post in enumerate(reversed(posts), 1):
                print(f"{i}. {post}")
    except Exception as e:
        print(f"An error occurred: {e}")
