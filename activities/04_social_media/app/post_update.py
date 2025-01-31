from users import users

def post_update():
    try:
        username = input("Enter your username: ")
        if username not in users:
            print("User not found. Please check your username.")
            return

        post = input("Enter your post: ")
        users[username]["posts"].append(post)
        print("Post added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
