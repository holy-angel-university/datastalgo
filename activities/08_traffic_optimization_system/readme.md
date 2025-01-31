# Traffic Optimization System

Your group is tasked with building a Traffic Optimization System for a city's traffic management department. The app should allow users to input traffic data, analyze traffic patterns, and optimize traffic light timings based on the number of cars passing through at different times and days. The system should handle multiple intersections and ensure that traffic light timings are adjusted to minimize congestion.

The city currently uses fixed traffic light timings, which often lead to congestion during peak hours. They need a digital solution that can:

1. Record traffic data (e.g., number of cars, time, and date) for different intersections.
2. Analyze traffic patterns to identify peak and off-peak hours.
3. Optimize traffic light timings based on historical traffic data.
4. Generate reports to visualize traffic patterns and optimized timings.

Your team is tasked with building a Python program that simulates the Traffic Optimization System. The program should allow users to interact with the system dynamically (e.g., input traffic data, analyze patterns, optimize timings) and provide real-time updates on traffic light adjustments.

## Key Features


1. **Input Traffic Data**

    - Allow users to input traffic data for a specific intersection, including the number of cars, time, and date.

2. **Analyze Traffic Patterns**

    - Analyze historical traffic data to identify peak and off-peak hours for each intersection.

3. **Optimize Traffic Light Timings**

    - Calculate optimized traffic light timings based on the number of cars passing through at different times and days.

4. **Generate Traffic Report**

    - Generate a report for a specific intersection, displaying traffic patterns and optimized traffic light timings.

5. **Dynamic Interaction**

    - Instead of a static menu, the app will prompt the user for actions dynamically (e.g., "What would you like to do next?").

6. **Error Handling**

    - Handle invalid inputs (e.g., non-numeric values for the number of cars) and display user-friendly error messages.

7. **Type Casting**

    - Convert user inputs (e.g., number of cars, time) to appropriate data types (e.g., `int`, `datetime`).

8. **Modularize**

    - Divide the program into functions to handle different operations.
    - Every function should have a clear purpose and return values as needed, and they should be separated from the main program logic.

## Interaction

```codeowners title="Example"
Welcome to the Traffic Optimization System!

What would you like to do? (input/analyze/optimize/report/exit): input
Enter intersection ID: 1
Enter number of cars: 50
Enter time (HH:MM): 08:30
Enter date (YYYY-MM-DD): 2023-10-01
Traffic data recorded successfully!

What would you like to do? (input/analyze/optimize/report/exit): analyze
Enter intersection ID: 1
Traffic Patterns for Intersection 1:
- Peak Hours: 08:00 - 09:00 (Average Cars: 60)
- Off-Peak Hours: 14:00 - 15:00 (Average Cars: 20)

What would you like to do? (input/analyze/optimize/report/exit): optimize
Enter intersection ID: 1
Optimized Traffic Light Timings for Intersection 1:
- Peak Hours: 08:00 - 09:00 (Green Light Duration: 90 seconds)
- Off-Peak Hours: 14:00 - 15:00 (Green Light Duration: 30 seconds)

What would you like to do? (input/analyze/optimize/report/exit): report
Enter intersection ID: 1
Traffic Report for Intersection 1:
- Total Cars Recorded: 500
- Peak Hours: 08:00 - 09:00 (Average Cars: 60)
- Off-Peak Hours: 14:00 - 15:00 (Average Cars: 20)
- Optimized Timings:
  - Peak Hours: 90 seconds
  - Off-Peak Hours: 30 seconds

What would you like to do? (input/analyze/optimize/report/exit): exit
Thank you for using the Traffic Optimization System!
```
