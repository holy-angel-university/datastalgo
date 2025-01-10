# Variables and Data Types

In Python, a variable is a name that refers to a value. Variables are used to store data that can be referenced and manipulated in a program. Python is dynamically typed, meaning you do not need to declare the type of a variable when you create it.

## Creating Variables

Variables are created the first time a value is assigned to them. You can assign a value to a variable using the assignment operator `=`. Here are some examples:

```python
age = 25
name = "Alice"
height = 5.6
is_student = True
```

## Naming Conventions

When naming variables, follow these rules:

- Variable names must start with a letter (a-z, A-Z) or an underscore (_).
- The rest of the name can contain letters, numbers (0-9), and underscores.
- Variable names are case-sensitive (`age` and `Age` are different).
- Avoid using Python reserved keywords (like `if`, `else`, `while`, etc.) as variable names.

Examples of valid variable names:

```python
my_variable = 42
userName = "Bob"
is_student = True
_age = 25
```

## Data Types

Python has several built-in data types:

- **Numeric**: `int`, `float`, `complex`
- **Sequence**: `str`, `list`, `tuple`, `range`
- **Mapping**: `dict`
- **Set**: `set`, `frozenset`
- **Boolean**: `bool`
- **Binary**: `bytes`, `bytearray`, `memoryview`

You can use the `type()` function to check the data type of a variable. Here are some examples:

```python
x = 5
y = 3.14

print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'float'>
```

## Type Conversion

You can convert between different data types using built-in functions like `int()`, `float()`, `str()`, etc. Here are some examples:

```python
x = 5
y = 3.14

x = float(x)
y = int(y)

print(x) # Output: 5.0
print(y) # Output: 3
```

## Constants

In Python, constants are usually defined as variables in all capital letters. While Python does not have built-in support for constants, this convention is used to indicate that a variable should not be changed. Here is an example:

```python
PI = 3.14159
GRAVITY = 9.81
```

## Conclusion

Understanding variables and data types is fundamental in Python programming. They allow you to store and manipulate data effectively.