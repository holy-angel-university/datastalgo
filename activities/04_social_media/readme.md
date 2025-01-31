# Social Media

Your group is tasked with building a Social Media App for a small community. The app should allow users to create profiles, post updates, view their feed, and interact with other users. The system should handle multiple users and ensure that operations like posting and viewing feeds are performed correctly.

The community currently uses manual methods to share updates, which is disorganized and lacks structure. They need a digital solution that can:

1. Allow users to create profiles with unique usernames.
2. Enable users to post updates and view their own feed.
3. Display a list of all users and their profiles.
3. Handle errors gracefully, such as invalid inputs or duplicate usernames.

Your team is tasked with building a Python program that simulates the Social Media App. The program should allow users to interact with the system dynamically (e.g., create profiles, post updates, view feeds) and provide real-time updates on user activity.

## Key Features

1. **Create Profile**

    - Allow users to create a profile with a unique username, name, and an empty list of posts.

2. **Post Update**

    - Allow users to post updates (e.g., "Hello, world!") and store them in their profile.

3. **View Feed**

    - Allow users to view their own feed (i.e., their posts) in reverse chronological order (newest first).

4. **View All Profiles**

    - Display a list of all users and their usernames.

5. **Menu-Driven Interface**

    - Display a menu with options for creating profiles, posting updates, viewing feeds, viewing all profiles, and exiting the program.

6. **Error Handling**

    - Handle invalid inputs (e.g., non-numeric values for menu choices) and display user-friendly error messages.

7. **Type Casting**

    - Convert user inputs (e.g., menu choices) to appropriate data types (e.g., int).

8. **Modularize**

    - Divide the program into functions to handle different operations.
    - Every function should have a clear purpose and return values as needed, and they should be separated from the main program logic.

## Interaction

```codeowners title="Example"
Welcome to the Social Media App!
1. Create Profile
2. Post Update
3. View My Feed
4. View All Profiles
5. Exit
Enter your choice: 1

Enter your username: johndoe
Enter your name: John Doe
Profile created successfully!

1. Create Profile
2. Post Update
3. View My Feed
4. View All Profiles
5. Exit
Enter your choice: 2

Enter your username: johndoe
Enter your post: Hello, world!
Post added successfully!

1. Create Profile
2. Post Update
3. View My Feed
4. View All Profiles
5. Exit
Enter your choice: 3

Enter your username: johndoe
Your Feed:
1. Hello, world!

1. Create Profile
2. Post Update
3. View My Feed
4. View All Profiles
5. Exit
Enter your choice: 4

All Profiles:
1. John Doe (johndoe)

1. Create Profile
2. Post Update
3. View My Feed
4. View All Profiles
5. Exit
Enter your choice: 5

Thank you for using the Social Media App!
```
