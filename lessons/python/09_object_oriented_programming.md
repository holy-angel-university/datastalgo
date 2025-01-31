# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. OOP helps in creating reusable, modular, and maintainable code by modeling real-world entities as objects with attributes (data) and methods (functions).

## Classes and Objects

### What is a Class?

A class is a blueprint for creating objects. It defines the attributes and methods that the objects will have.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")
```

### What is an Object?

An object is an instance of a class. It represents a specific entity based on the class blueprint.

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()  # Output: Buddy says woof!
dog2.bark()  # Output: Max says woof!
```

## Attributes and Methods

### Attributes

Attributes are variables that belong to an object. They represent the state or data of the object.

```python
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3
```

### Methods

Methods are functions that belong to an object. They represent the behavior or actions of the object.

```python
dog1.bark()  # Output: Buddy says woof!
```

## The `__init__` Method

The `__init__ `method is a special method called a constructor. It is automatically executed when a new object is created. It is used to initialize the object's attributes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```


## Inheritance

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). It promotes code reuse and establishes a relationship between classes.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

dog = Dog("Buddy")
dog.speak()  # Output: Buddy says woof!
```

## Method Overriding

Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class.

```python
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")

cat = Cat("Whiskers")
cat.speak()  # Output: Whiskers says meow!
```

## Encapsulation

Encapsulation is the concept of restricting access to certain attributes or methods to protect the internal state of an object. In Python, encapsulation is achieved using private attributes (prefixed with `_` or `__`) and getter/setter methods.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables flexibility and dynamic behavior.

```python
def animal_sound(animal):
    animal.speak()

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # Output: Buddy says woof!
animal_sound(cat)  # Output: Whiskers says meow!
```

## Class and Static Methods

- **Class Methods**: Methods that are bound to the class rather than the instance. They can modify class-level attributes.
- **Static Methods**: Methods that do not depend on the instance or class. They are used for utility functions.

```python
class MathOperations:
    @classmethod
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.multiply(3, 4))  # Output: 12
print(MathOperations.add(3, 4))       # Output: 7
```

## Special Methods

Special methods (or magic methods) allow you to define how objects behave with built-in operations like `+`, `-`, `==`, etc.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
```

Object-Oriented Programming is a powerful paradigm that helps in organizing code, promoting reusability, and modeling real-world problems effectively. By mastering classes, objects, inheritance, encapsulation, and polymorphism, your students will be able to write clean, modular, and maintainable code.