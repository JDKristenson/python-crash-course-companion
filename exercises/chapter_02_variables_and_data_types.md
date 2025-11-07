# Chapter 2: Variables and Simple Data Types

## Learning Objectives
- Understand variables and naming conventions
- Work with strings and string methods
- Use integers and floats
- Handle comments in code

## Key Concepts
- Variable naming rules
- String methods (upper, lower, title, strip, etc.)
- f-strings (formatted string literals)
- Integers and floats
- Comments

## Try It Yourself Exercises

### 2-1: Simple Message
Assign a message to a variable, and print that message.

### 2-2: Simple Messages
Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.

### 2-3: Personal Message
Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as "Hello Eric, would you like to learn some Python today?"

### 2-4: Name Cases
Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.

### 2-5: Famous Quote
Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like: `Albert Einstein once said, "A person who never made a mistake never tried anything new."`

### 2-6: Famous Quote 2
Repeat Exercise 2-5, but this time, represent the famous person's name using a variable called `famous_person`. Then compose your message and represent it with a new variable called `message`. Print your message.

### 2-7: Stripping Names
Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Use `\t` and `\n` to add tabs and newlines. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions: lstrip(), rstrip(), and strip().

### 2-8: File Extensions
Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

### 2-9: Number Eight
Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results.

### 2-10: Favorite Number
Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.

### 2-11: Adding Comments
Choose two of the programs you've written, and add at least one comment to each. If you don't have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.

### 2-12: Zen of Python
Enter `import this` into a Python terminal session and skim through the additional principles.

## Quick Reference

### Variables
```python
message = "Hello Python world!"
x = 5
pi = 3.14159
```

### String Methods
```python
name = "ada lovelace"
print(name.title())      # Ada Lovelace
print(name.upper())      # ADA LOVELACE
print(name.lower())      # ada lovelace

# Stripping whitespace
favorite_language = ' python '
print(favorite_language.rstrip())   # ' python'
print(favorite_language.lstrip())   # 'python '
print(favorite_language.strip())    # 'python'

# Remove prefix/suffix
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))  # nostarch.com
```

### F-Strings
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
```

### Numbers
```python
# Integers
2 + 3     # 5
3 - 2     # 1
2 * 3     # 6
3 / 2     # 1.5
3 ** 2    # 9 (exponent)
3 // 2    # 1 (floor division)
10 % 3    # 1 (modulo)

# Floats
0.1 + 0.1   # 0.2
2 * 0.1     # 0.2

# Underscores in large numbers
universe_age = 14_000_000_000
```

### Comments
```python
# This is a comment
print("This will run")  # This is also a comment
```

## Common Mistakes
- Forgetting quotes around strings
- Mixing up variable names (case-sensitive!)
- Not closing quotes or parentheses
- Using keywords as variable names

## Practice Ideas
1. Create variables for your name, age, and favorite hobby
2. Practice all string methods on different strings
3. Calculate your age in days, hours, and minutes
4. Create a "business card" using f-strings with your info

## Book Resources Location
See: `book_resources/chapter_02/` for author's examples

## Your Workspace
Work on exercises here: `my_work/part_1_basics/chapters/chapter_02/`
