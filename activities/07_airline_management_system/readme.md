# Airlines Management System

Your group is tasked with building an Airlines Management System for a small airline company. The app should allow users to manage flights, book tickets, track passenger information, and generate reports. The system should handle multiple flights, passengers, and bookings, and ensure that operations are performed correctly.

The airline currently uses manual methods to manage flights and bookings, which is inefficient and prone to errors. They need a digital solution that can:

1. Add new flights with unique flight numbers, destinations, and seat capacities.
2. Allow passengers to book tickets for specific flights.
3. Track passenger information and update flight seat availability in real-time.
4. Generate reports for flight occupancy and revenue.

Your team is tasked with building a Python program that simulates the Airlines Management System. The program should allow users to interact with the system dynamically (e.g., add flights, book tickets, view flight details) and provide real-time updates on flight status and bookings.

## Key Features

1. **Add Flight**

    - Allow users to add a new flight with a unique flight number, destination, and seat capacity.

2. **Book Ticket**

    - Allow passengers to book tickets for a specific flight by providing their name and the flight number.
    - Update the flight's seat availability and store passenger information.

3. **View Flight Details**

    - Display the details of a specific flight, including destination, available seats, and passenger list.

4. **Generate Flight Report**

    - Generate a report for a specific flight, displaying its occupancy and revenue.

5. **Dynamic Interaction**

    - Instead of a static menu, the app will prompt the user for actions dynamically (e.g., "What would you like to do next?").

6. **Error Handling**

    - Handle invalid inputs (e.g., non-numeric values for flight numbers or seat counts) and display user-friendly error messages.

7. **Type Casting**

    Convert user inputs (e.g., flight numbers, seat counts) to appropriate data types (e.g., `int`).

8. **Modularize**

    - Divide the program into functions to handle different operations.
    - Every function should have a clear purpose and return values as needed, and they should be separated from the main program logic.

## Interaction

```codeowners title="Example"
Welcome to the Airlines Management System!

What would you like to do? (add/book/view/report/exit): add
Enter flight number: 101
Enter destination: New York
Enter seat capacity: 150
Flight added successfully!

What would you like to do? (add/book/view/report/exit): book
Enter flight number: 101
Enter passenger name: John Doe
Ticket booked successfully! Seat number: 1

What would you like to do? (add/book/view/report/exit): view
Enter flight number: 101
Flight Details:
- Destination: New York
- Available Seats: 149
- Passengers:
  1. John Doe (Seat: 1)

What would you like to do? (add/book/view/report/exit): report
Enter flight number: 101
Flight Report:
- Destination: New York
- Total Seats: 150
- Booked Seats: 1
- Available Seats: 149
- Revenue: $200.0

What would you like to do? (add/book/view/report/exit): exit
Thank you for using the Airlines Management System!
```