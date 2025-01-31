# Environmental Impact Analysis and Optimization System

Your group is tasked with building an Environmental Impact Analysis and Optimization System for a sustainability-focused organization. The app should allow users to input environmental data, analyze the impact of their activities, optimize resource usage, and provide actionable recommendations to reduce their carbon footprint and waste production.

The organization currently lacks a systematic way to track and analyze its environmental impact. They need a digital solution that can:

1. Record environmental data (e.g., carbon emissions, energy usage, waste production) for different activities or time periods.
2. Analyze the environmental impact of activities to identify areas for improvement.
3. Optimize resource usage to minimize environmental impact.
4. Provide recommendations for sustainable practices (e.g., renewable energy, recycling, waste reduction).

Your team is tasked with building a Python program that simulates the Environmental Impact Analysis and Optimization System. The program should allow users to interact with the system dynamically (e.g., input data, analyze impact, optimize usage) and provide real-time recommendations for sustainability.

## Key Features

1. **Input Environmental Data**

    - Allow users to input environmental data for a specific activity or time period, including carbon emissions, energy usage, and waste production.

2. **Analyze Environmental Impact**

    - Analyze the environmental impact of activities to identify areas with the highest carbon footprint, energy consumption, or waste production.

3. **Optimize Resource Usage**

    - Calculate optimized resource usage to minimize environmental impact (e.g., reduce energy consumption, increase recycling).

4. **Provide Recommendations**

    - Provide actionable recommendations for sustainable practices (e.g., switch to renewable energy, reduce waste, improve recycling).

5. **Dynamic Interaction**

    - Instead of a static menu, the app will prompt the user for actions dynamically (e.g., "What would you like to do next?").

6. **Error Handling**

    - Handle invalid inputs (e.g., non-numeric values for carbon emissions or energy usage) and display user-friendly error messages.

7. **Type Casting**

    - Convert user inputs (e.g., carbon emissions, energy usage) to appropriate data types (e.g., `float`).

8. **Modularize**

    - Divide the program into functions to handle different operations.
    - Every function should have a clear purpose and return values as needed, and they should be separated from the main program logic.

## Interaction

```codeowners title="Example"
Welcome to the Environmental Impact Analysis and Optimization System!

What would you like to do? (input/analyze/optimize/recommend/exit): input
Enter activity name: Office Operations
Enter carbon emissions (in tons): 5.2
Enter energy usage (in kWh): 1200
Enter waste production (in kg): 150
Environmental data recorded successfully!

What would you like to do? (input/analyze/optimize/recommend/exit): analyze
Environmental Impact Analysis:
- Highest Carbon Footprint: Office Operations (5.2 tons)
- Highest Energy Usage: Office Operations (1200 kWh)
- Highest Waste Production: Office Operations (150 kg)

What would you like to do? (input/analyze/optimize/recommend/exit): optimize
Optimized Resource Usage:
- Reduce energy usage by 20% (960 kWh).
- Increase recycling rate by 30% (waste reduced to 105 kg).

What would you like to do? (input/analyze/optimize/recommend/exit): recommend
Recommendations for Office Operations:
1. Switch to renewable energy sources (e.g., solar panels).
2. Implement a recycling program to reduce waste production.
3. Use energy-efficient appliances to lower energy consumption.

What would you like to do? (input/analyze/optimize/recommend/exit): exit
Thank you for using the Environmental Impact Analysis and Optimization System!
```
