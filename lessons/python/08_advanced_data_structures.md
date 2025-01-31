# Advanced Data Structures

In Python, data structures are used to store and organize data efficiently. This lesson will dive deeper into advanced features and introduce sets. These structures are essential for handling complex data and solving real-world problems.

## Lists

Lists are ordered, mutable collections of items. They are one of the most versatile data structures in Python and support a wide range of operations.

### Key Featres of Lists

1. **Mutable**: You can change, add, or remove elements after creation.
2. **Ordered**: Elements are stored in a specific order, and you can access them using indices.
3. **Heterogeneous**: Lists can store elements of different data types (e.g., integers, strings, other lists).

### Advanced List Operations

#### 1. List Comprehensions

A concise way to create lists.

```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### 2. Slicing

Extract a portion of a list using the syntax `list[start:stop:step]`.

- `start`: The index where the slice begins.
- `stop`: The index where the slice ends (exclusive).
- `step`: The increment between elements.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])  # Output: [2, 3, 4, 5, 6]
print(numbers[::2])  # Output: [0, 2, 4, 6, 8]
```

#### 3. Common Methods

- `append()`: Add an element to the end of the list.
- `extend()`: Add elements from another list to the end.
- `insert()`: Insert an element at a specific index.
- `remove()`: Remove the first occurrence of an element.
- `pop()`: Remove and return an element by index.
- `sort()`: Sort the list in ascending order.
- `reverse()`: Reverse the order of elements.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'orange']
```

## Tuples

Tuples are ordered, immutable collections of items. They are similar to lists but cannot be modified after creation.

### Key Features of Tuples

- **Immutable**: Once created, elements cannot be added, removed, or changed.
- **Ordered**: Elements are stored in a specific order and can be accessed using indices.
- **Heterogeneous**: Tuples can store elements of different data types.

### Advanced Tuple Operations

#### 1. Packing and Unpacking

Assign multiple values to a single variable (packing) and extract them into separate variables (unpacking).

```python
person = ("Alice", 30, "New York")
name, age, city = person
print(name)  # Output: Alice
```

#### 2. Tuple Comprehensions

Tuples do not have a built-in comprehension syntax, but you can use a generator expression to create them.

```python
squares = tuple(x**2 for x in range(10))
print(squares)  # Output: (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
```

## Dictionaries

Dictionaries are unordered collections of key-value pairs. They are highly efficient for looking up values based on unique keys.

### Key Features of Dictionaries

- **Mutable**: You can add, remove, or modify key-value pairs.
- **Unordered**: Elements are not stored in a specific order (prior to Python 3.7).
- **Keys Must Be Unique**: Each key maps to exactly one value.

### Advanced Dictionary Operations

#### 1. Dictionary Comprehensions

Create dictionaries using a concise syntax.

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### 2. Common Methods

- `get()`: Retrieve a value by key, returning `None` if the key is not found.
- `keys()`: Get a view of all keys in the dictionary.
- `values()`: Get a view of all values in the dictionary.
- `items()`: Get a view of all key-value pairs in the dictionary.
- `update()`: Merge another dictionary into the current one.

```python
student = {"name": "Alice", "age": 25, "major": "Computer Science"}
print(student.keys())  # Output: dict_keys(['name', 'age', 'major'])
print(student.get("age"))  # Output: 25
student.update({"age": 26, "year": 3})
print(student)  # Output: {'name': 'Alice', 'age': 26, 'major': 'Computer Science', 'year': 3}
```

## Sets

Sets are unordered collections of unique elements. They are useful for performing mathematical operations like unions, intersections, and differences.

### Key Features of Sets

- **Mutable**: You can add or remove elements.
- **Unordered**: Elements are not stored in a specific order.
- **Unique Elements**: Sets automatically remove duplicate values.

### Advanced Set Operations

#### 1. Set Operations

- **Union**: Combine elements from two sets.
- **Intersection**: Find common elements between two sets.
- **Difference**: Find elements in one set but not the other.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # Output: {3, 4}
print(set1.difference(set2))  # Output: {1, 2}
```

#### 2. Common Methods

- `add()`: Add an element to the set.
- `remove()`: Remove an element from the set.
- `discard()`: Remove an element if it exists (does not raise an error if the element is not found).
- `pop()`: Remove and return an arbitrary element.

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}
```

## Conclusion

Understanding advanced data structures like lists, tuples, dictionaries, and sets is crucial for writing efficient and organized Python programs. These structures allow you to handle complex data and perform operations like filtering, sorting, and mathematical computations with ease.