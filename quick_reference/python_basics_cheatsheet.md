# Python Basics Cheat Sheet

## Variables and Data Types

### Variables
```python
message = "Hello"
age = 25
price = 19.99
is_student = True
```

### Strings
```python
# String methods
name = "ada lovelace"
name.title()          # "Ada Lovelace"
name.upper()          # "ADA LOVELACE"
name.lower()          # "ada lovelace"
name.strip()          # Remove whitespace
name.lstrip()         # Remove left whitespace
name.rstrip()         # Remove right whitespace

# F-strings (formatted strings)
first = "Ada"
last = "Lovelace"
full = f"{first} {last}"
message = f"Hello, {full.title()}!"
```

### Numbers
```python
# Integers
2 + 3      # Addition: 5
3 - 2      # Subtraction: 1
2 * 3      # Multiplication: 6
3 / 2      # Division: 1.5
3 ** 2     # Exponent: 9
3 // 2     # Floor division: 1
10 % 3     # Modulo: 1

# Floats
0.1 + 0.1  # 0.2
```

## Lists

### Creating and Accessing
```python
bicycles = ['trek', 'cannondale', 'redline']
print(bicycles[0])       # 'trek'
print(bicycles[-1])      # 'redline' (last item)
print(bicycles[0:2])     # ['trek', 'cannondale'] (slicing)
```

### Modifying Lists
```python
# Adding elements
bicycles.append('specialized')        # Add to end
bicycles.insert(0, 'giant')          # Insert at position

# Removing elements
bicycles.remove('redline')            # Remove by value
popped = bicycles.pop()               # Remove last item
popped = bicycles.pop(0)              # Remove by index
del bicycles[0]                       # Delete by index

# Sorting
bicycles.sort()                       # Sort permanently
bicycles.sort(reverse=True)           # Reverse sort
sorted(bicycles)                      # Sort temporarily
bicycles.reverse()                    # Reverse order
```

### List Operations
```python
len(bicycles)                         # Length
min([1, 2, 3])                       # Minimum
max([1, 2, 3])                       # Maximum
sum([1, 2, 3])                       # Sum
range(1, 5)                          # Generates 1,2,3,4
list(range(1, 5))                    # [1, 2, 3, 4]
```

## Loops

### For Loops
```python
# Loop through list
for bicycle in bicycles:
    print(bicycle)

# Loop with range
for number in range(1, 5):
    print(number)

# List comprehension
squares = [x**2 for x in range(1, 11)]
```

### While Loops
```python
count = 1
while count <= 5:
    print(count)
    count += 1

# With break
while True:
    message = input("Enter 'quit' to exit: ")
    if message == 'quit':
        break
    print(message)

# With continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

## Conditionals

### If Statements
```python
age = 19
if age >= 18:
    print("You can vote!")

# if-else
if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote.")

# if-elif-else
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
```

### Conditional Tests
```python
# Equality
car == 'bmw'           # True if equal
car != 'audi'          # True if not equal

# Numerical comparisons
age < 21
age <= 21
age > 21
age >= 21

# Multiple conditions
age >= 18 and age <= 65
age < 18 or age > 65

# Check if in list
'trek' in bicycles     # True if in list
'giant' not in bicycles  # True if not in list

# Check if list is empty
if bicycles:           # True if list has items
if not bicycles:       # True if list is empty
```

## Dictionaries

### Creating and Accessing
```python
alien = {'color': 'green', 'points': 5}
print(alien['color'])           # 'green'
print(alien.get('color'))       # 'green'
print(alien.get('speed', 0))    # 0 (default if not found)

# Adding/modifying
alien['x_position'] = 0
alien['color'] = 'yellow'

# Removing
del alien['points']
popped = alien.pop('color')
```

### Looping Through Dictionaries
```python
# Loop through key-value pairs
for key, value in alien.items():
    print(f"Key: {key}, Value: {value}")

# Loop through keys
for key in alien.keys():
    print(key)

# Loop through values
for value in alien.values():
    print(value)

# Loop through values (no duplicates)
for value in set(alien.values()):
    print(value)
```

## Functions

### Defining Functions
```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# With parameter
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# With return value
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

# With default parameter
def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type} named {pet_name}.")

# Multiple return values
def get_name():
    return first_name, last_name
```

### Function Arguments
```python
# Positional arguments
describe_pet('harry', 'hamster')

# Keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')

# Arbitrary arguments
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)

make_pizza('pepperoni', 'mushrooms', 'peppers')

# Arbitrary keyword arguments
def build_profile(**user_info):
    return user_info

user = build_profile(first='albert', last='einstein', location='princeton')
```

## Files

### Reading Files
```python
# Read entire file
with open('file.txt') as file:
    contents = file.read()
    print(contents)

# Read line by line
with open('file.txt') as file:
    for line in file:
        print(line.rstrip())

# Read into list
with open('file.txt') as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write (overwrites)
with open('file.txt', 'w') as file:
    file.write("I love programming.\n")

# Append
with open('file.txt', 'a') as file:
    file.write("I love Python.\n")
```

## Exception Handling

```python
# Basic try-except
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Multiple exceptions
try:
    # risky code
    pass
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid value")

# Silent failure
try:
    # risky code
    pass
except FileNotFoundError:
    pass  # Do nothing

# else clause
try:
    result = 5 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(result)  # Runs if no exception
```

## Classes

```python
class Dog:
    """A simple dog class."""
    
    def __init__(self, name, age):
        """Initialize attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate sitting."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over."""
        print(f"{self.name} rolled over!")

# Creating instances
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
my_dog.sit()
my_dog.roll_over()

# Inheritance
class Puppy(Dog):
    """Represents a young dog."""
    
    def __init__(self, name, age):
        """Initialize parent class."""
        super().__init__(name, age)
        self.trained = False
```

## Useful Built-in Functions

```python
len(list)           # Length
type(variable)      # Type of variable
str(number)         # Convert to string
int(string)         # Convert to integer
float(string)       # Convert to float
input("Prompt: ")   # Get user input
print(value)        # Print to console
range(start, stop)  # Generate range
sorted(list)        # Return sorted copy
reversed(list)      # Return reversed iterator
enumerate(list)     # Get index and value in loop
zip(list1, list2)   # Combine lists
```
