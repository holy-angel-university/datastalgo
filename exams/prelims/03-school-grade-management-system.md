# School Grade Management System

You are tasked with creating a Python program to manage and analyze the grades of students in a class.

## Requirements

- Use variables to store student names and their grades in multiple subjects (e.g., Math, Science, English).
- Use a loop to collect data for multiple students (e.g., 5 students).
- Use conditionals (`if-else`) to determine the final grade based on the average:
  - **A**: 90% and above
  - **B**: 80% to 89%
  - **C**: 70% to 79%
  - **D**: 60% to 69%
  - **F**: Below 60%
- Use type casting to convert user input (which is initially a string) into appropriate data types (float or int).
- Use a function to calculate the average grade and determine the final grade.
- Track the top-performing student (highest average) and display their details at the end.

## Example Output

```plaintext
Enter the number of students: 3
Enter the number of subjects: 4

Enter details for Student 1:
Name: A
Grade for Subject 1: 85
Grade for Subject 2: 90
Grade for Subject 3: 88
Grade for Subject 4: 90

Enter details for Student 2:
Name: B
Grade for Subject 1: 78
Grade for Subject 2: 89
Grade for Subject 3: 79
Grade for Subject 4: 90

Enter details for Student 3:
Name: C
Grade for Subject 1: 89
Grade for Subject 2: 86
Grade for Subject 3: 85
Grade for Subject 4: 94

Student Report:
- A: Average = 88.25, Grade = B
- B: Average = 84.00, Grade = B
- C: Average = 88.50, Grade = B

Top-performing student: C with an average of 88.50!
```

## Hints

- Use nested loops: an outer loop for students and an inner loop for subjects.
- Use a dictionary or list to store student data (e.g., name, grades, average, and final grade).
- Use the `max()` function or a custom loop to find the top-performing student.
- Use `try-except` to handle invalid input.
