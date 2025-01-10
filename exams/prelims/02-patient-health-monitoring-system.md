# Patient Health Monitoring System

## Scenario

You are tasked with creating a program that monitors a patient's health based on their vital signs. The program will take input for the patient's temperature, heart rate, and oxygen level, and then determine if the patient is in a healthy state or needs medical attention.

## Requirements

1. Use variables to store the patient's temperature (in Celsius), heart rate (in BPM), and oxygen level (in percentage).
2. Use conditionals (if-else) to check if the patient's vital signs are within normal ranges:
   - Temperature should be between 36.1°C and 37.2°C.
   - Heart rate should be between 60 BPM and 100 BPM.
   - Oxygen level should be between 95% and 100%.
2. Use type casting to convert user input (which is initially a string) into appropriate data types (float or int).
3. Use a function to check and display the patient's health status.

## Example Outputs

```plaintext
Enter patient's temperature (in Celsius): 37.5
Enter patient's heart rate (in BPM): 110
Enter patient's oxygen level (in percentage): 92

Patient Health Status:
- Temperature: High
- Heart Rate: High
- Oxygen Level: Low
This patient needs medical attention!
```

```plaintext
Enter patient's temperature (in Celsius): 36.5
Enter patient's heart rate (in BPM): 75
Enter patient's oxygen level (in percentage): 98
## Your Task  

- Write a Python program that meets the requirements above.
- Ensure the program handles invalid input (e.g., non-numeric values) gracefully.
- Add a function to encapsulate the logic for checking and displaying the patient's health status.
This patient is healthy!
```

## Hints

- Use `input()` to get user input and `float()` or `int()` for type casting.
- Use nested `if-else` statements to check multiple conditions.
- Define a function like `check_health_status(temperature, heart_rate, oxygen_level)` to modularize your code.