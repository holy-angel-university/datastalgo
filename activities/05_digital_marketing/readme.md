# Digital Marketing

Your group is tasked with building a Digital Marketing Business App for a small marketing agency. The app should allow users to manage clients, create marketing campaigns, track campaign performance, and generate reports. The system should handle multiple clients and campaigns and ensure that operations are performed correctly.

The agency currently uses manual methods to track clients and campaigns, which is inefficient and error-prone. They need a digital solution that can:

1. Add new clients with unique client IDs and contact information.
2. Create marketing campaigns for specific clients with performance metrics (e.g., impressions, clicks, conversions).
3. Track and update campaign performance in real-time.
4. Generate reports for specific campaigns to analyze their performance.

Your team is tasked with building a Python program that simulates the Digital Marketing Business App. The program should allow users to interact with the system dynamically (e.g., add clients, create campaigns, track performance) and provide real-time updates on campaign metrics.

## Key Features

1. **Add Client**

    - Allow users to add a new client with a unique client ID, name, and email.

2. **Create Campaign**

    - Allow users to create a new campaign for a specific client. The campaign should have a unique campaign ID, name, and initial performance metrics.

3. **Track Campaign Performance**

    - Allow users to update campaign performance metrics (e.g., impressions, clicks, conversions).

4. **Generate Report**

    - Generate a report for a specific campaign, displaying its performance metrics.

5. **Menu-Driven Interface**

    - Display a menu with options for adding clients, creating campaigns, tracking performance, generating reports, and exiting the program.

6. **Error Handling**

    - Handle invalid inputs (e.g., non-numeric values for metrics) and display user-friendly error messages.

7. **Type Casting**

    - Convert user inputs (e.g., metrics) to appropriate data types (e.g., int for impressions).

8. **Modularize**

    - Divide the program into functions to handle different operations.
    - Every function should have a clear purpose and return values as needed, and they should be separated from the main program logic.

## Interaction

```codeowners title="Example"
Welcome to the Digital Marketing Business App!
1. Add Client
2. Create Campaign
3. Track Campaign Performance
4. Generate Report
5. Exit
Enter your choice: 1

Enter client ID: 101
Enter client name: John Doe
Enter client email: john.doe@example.com
Client added successfully!

1. Add Client
2. Create Campaign
3. Track Campaign Performance
4. Generate Report
5. Exit
Enter your choice: 2

Enter campaign ID: 201
Enter client ID: 101
Enter campaign name: Summer Sale
Enter initial impressions: 1000
Enter initial clicks: 100
Enter initial conversions: 10
Campaign created successfully!

1. Add Client
2. Create Campaign
3. Track Campaign Performance
4. Generate Report
5. Exit
Enter your choice: 3

Enter campaign ID: 201
Enter new impressions: 1500
Enter new clicks: 150
Enter new conversions: 15
Campaign performance updated successfully!

1. Add Client
2. Create Campaign
3. Track Campaign Performance
4. Generate Report
5. Exit
Enter your choice: 4

Enter campaign ID: 201
Campaign Report:
- Campaign Name: Summer Sale
- Impressions: 1500
- Clicks: 150
- Conversions: 15

1. Add Client
2. Create Campaign
3. Track Campaign Performance
4. Generate Report
5. Exit
Enter your choice: 5

Thank you for using the Digital Marketing Business App!
```
