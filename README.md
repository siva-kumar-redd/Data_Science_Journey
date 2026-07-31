# Data Scientist
Aspiring Data Scientist with a strong interest in Python, Data Analysis, and Machine Learning.   Passionate about building real-world projects, solving problems, and continuously improving technical skills through hands-on learning and development.

# 🎓 Day 1 — Python Foundations & ML Journey

## 🚀 Goal of Day 1

Today I started my journey toward becoming an Data Scientist.

### Objectives
- ✅ Set up development environment
- ✅ Learn Python fundamentals
- ✅ Write beginner programs
- ✅ Create GitHub profile
- ✅ Build first mini project

---

# 📚 What I Learned Today

## 📦 Variables

Variables are used to store data.

```python
name = "Siva"
age = 22
```

## 🔢 Data Types

| Type | Example |
|--------|---------|
| String | "Siva" |
| Integer | 22 |
| Float | 5.8 |
| Boolean | True |

```python
name = "Siva"
age = 22
height = 5.8
is_student = True
```

## ⌨️ Input & Output

```python
name = input("Enter your name: ")
print("Hello", name)
```

## ➕ Arithmetic Operators

```python
a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

## 🐍 Basic Python Syntax

Learned:
- Variables
- Data Types
- User Input
- Print Statements
- Comments
- Arithmetic Operations

---

# 🧠 Practice Programs Completed

- ✅ Variables Program
- ✅ Data Types Program
- ✅ Input & Output Program
- ✅ Add Two Numbers
- ✅ Simple Calculator

---

# 💻 Mini Project

## Simple Calculator

Features:
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division

---

# 🚀 Why This Matters

These concepts are the foundation of:

- 🤖 Machine Learning Models
- 📊 Data Analysis
- 🔄 Data Pipelines
- 🧠 Artificial Intelligence Applications

Every Data Scientist starts by mastering Python fundamentals.

# 🚀 Day 2 — Decision Making in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Beginner-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-2-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Decision%20Making-orange?style=for-the-badge)

</div>

---

# 🎯 Goal of Day 2

Today I learned how computers make decisions using conditions in Python.

By the end of today, I can:

✅ Write conditional statements  
✅ Use comparison operators  
✅ Use logical operators  
✅ Build decision-making programs  
✅ Improve programming logic

---

# 📚 Topics Covered

## 🔹 Comparison Operators

Used to compare values.

| Operator | Meaning |
|-----------|----------|
| `==` | Equal to |
| `!=` | Not Equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or Equal |
| `<=` | Less than or Equal |

Example:

```python
a = 10
b = 20

print(a < b)
```

---

## 🔹 If Statement

```python
age = 18

if age >= 18:
    print("Eligible to Vote")
```

---

## 🔹 If-Else Statement

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## 🔹 If-Elif-Else Statement

```python
marks = 85

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
else:
    print("C Grade")
```

---

## 🔹 Nested If

```python
age = 20

if age >= 18:
    if age <= 60:
        print("Adult")
```

---

## 🔹 Logical Operators

### AND

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

### OR

```python
if age >= 18 or citizen:
    print("Allowed")
```

### NOT

```python
is_raining = False

if not is_raining:
    print("Go Outside")
```

---

# 🚀 Day 3 — Loops, Patterns & Logic Building

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-3-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Loops%20%26%20Patterns-orange?style=for-the-badge)

### 🔥 Training the Programmer's Mind Through Repetition

</div>

---

# 🎯 Goal of Day 3

Today I learned how to make programs repeat tasks efficiently using loops.

By the end of today, I can:

✅ Use `for` loops  
✅ Use `while` loops  
✅ Understand `range()`  
✅ Perform reverse iteration  
✅ Build patterns using nested loops  
✅ Understand basic time complexity

---

# 📚 What I Learned Today

## 🔄 For Loop

Used when the number of iterations is known.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## 🔄 While Loop

Used when the number of iterations is unknown.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 📍 range()

Generates a sequence of numbers.

### Basic Range

```python
for i in range(5):
    print(i)
```

### Start & Stop

```python
for i in range(1, 6):
    print(i)
```

### Start, Stop & Step

```python
for i in range(1, 11, 2):
    print(i)
```

---

## ⏪ Reverse Iteration

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

---

## 🔁 Nested Loops

A loop inside another loop.

```python
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
```

Output:

```text
* * *
* * *
* * *
```

---

# ⭐ Pattern Building

## Square Pattern

```text
* * * *
* * * *
* * * *
* * * *
```

---

## Triangle Pattern

```text
*
* *
* * *
* * * *
```

---

## Number Pattern

```text
1
1 2
1 2 3
1 2 3 4
```

---

## Multiplication Table

```python
for i in range(1, 11):
    print("5 x", i, "=", 5*i)
```

---



# ⚡ First Exposure to Time Complexity

Time Complexity tells us how efficiently a program runs.

## O(n)

Single Loop

```python
for i in range(n):
    print(i)
```

Complexity:

```text
O(n)
```

---

## O(n²)

Nested Loops

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Complexity:

```text
O(n²)
```
# 🚀 Day 4 — Functions in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-4-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Functions-orange?style=for-the-badge)

### 🔥 Learning to Write Reusable and Professional Code

</div>

---

# 🎯 Goal of Day 4

Today I learned how to write reusable code using functions.

By the end of today, I can:

✅ Create functions  
✅ Pass parameters and arguments  
✅ Return values from functions  
✅ Understand variable scope  
✅ Build reusable programs  

---

# 📚 What I Learned Today

## 🔹 Function Basics

Functions help organize code into reusable blocks.

```python
def greet():
    print("Hello AI Engineer")

greet()
```

---

## 🔹 Parameters and Arguments

Functions can accept input values.

```python
def greet(name):
    print("Hello", name)

greet("Siva")
```

---

## 🔹 Return Values

Functions can return results.

```python
def square(num):
    return num * num

result = square(5)

print(result)
```

Output:

```text
25
```

---

## 🔹 Variable Scope

### Global Variable

```python
name = "Siva"

def show_name():
    print(name)

show_name()
```

### Local Variable

```python
def demo():
    age = 21
    print(age)

demo()
```

---

# 💻 Programs Implemented

## Welcome Function

```python
def welcome():
    print("Welcome to AI/Data Scientisting")

welcome()
```

---

## Motivation Function

```python
def motivation():
    print("Never Stop Learning")

motivation()
```

---

## Student Function

```python
def student(name, age):
    print(name, age)

student("Siva", 21)
```

---

## Square Function

```python
def square(n):
    return n * n

print(square(5))
```

---

## Prediction System

```python
def prediction(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

print(prediction(75))
print(prediction(20))
```

---

# 🧠 Practice Programs Completed

- ✅ Welcome Function
- ✅ Motivation Function
- ✅ Student Function
- ✅ Square Calculator
- ✅ Prediction System
- ✅ Scope Demonstration

---

# 🏢 Real-World AI/ML Connection

Functions are heavily used in:

- 🤖 Machine Learning Pipelines
- 📊 Data Analysis
- 🧠 AI Applications
- 🌐 APIs
- ☁️ Production Systems

Example:

```python
def load_data():
    pass

def preprocess_data():
    pass

def train_model():
    pass

def evaluate_model():
    pass

def predict():
    pass


# 🚀 Day 5 — Lists in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-5-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Lists-orange?style=for-the-badge)

### 🔥 Learning to Store, Manage & Analyze Collections of Data

</div>

---

# 🎯 Goal of Day 5

Today I learned how to store and process multiple values using Python Lists.

By the end of today, I can:

✅ Create Lists  
✅ Access Elements using Indexing  
✅ Modify Lists  
✅ Traverse Lists using Loops  
✅ Analyze Datasets using Lists  
✅ Build Real-World Data Analytics Programs

---

# 📚 What I Learned Today

## 🔹 Introduction to Lists

Lists allow us to store multiple values in a single variable.

```python
marks = [78, 92, 45, 88]
```

---

## 🔹 Accessing Elements

### Positive Indexing

```python
print(marks[0])
```

Output:

```text
78
```

### Negative Indexing

```python
print(marks[-1])
```

Output:

```text
88
```

---

## 🔹 List Operations

### append()

Adds an element to the end of a list.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

---

### insert()

Adds an element at a specific position.

```python
cities = ["Guntur", "Bangalore"]

cities.insert(1, "Hyderabad")

print(cities)
```

---

### remove()

Removes a specific value.

```python
data = [100, 200, 300, 400]

data.remove(300)

print(data)
```

---

### pop()

Removes an element by index.

```python
nums = [10, 20, 30]

nums.pop()

print(nums)
```

Output:

```text
[10, 20]
```

---

# 🔄 Traversing Lists

Traversing means visiting every element one by one.

```python
nums = [5, 10, 15, 20]

for num in nums:
    print(num)
```

Output:

```text
5
10
15
20
```

---

# 📊 List Analytics

## Sum of Elements

```python
nums = [10, 20, 30, 40]

total = 0

for num in nums:
    total += num

print(total)
```

Output:

```text
100
```

---

## Count Elements Greater Than a Value

```python
nums = [10, 20, 30, 40, 50]

count = 0

for num in nums:
    if num > 25:
        count += 1

print(count)
```

Output:

```text
3
```

---

## Search in a List

```python
nums = [10, 20, 30, 40]

if 25 in nums:
    print("Found")
else:
    print("Not Found")
```

Output:

```text
Not Found
```

---

# 💻 Mini Project — Student Marks Analyzer

Dataset:

```python
marks = [65, 78, 92, 35, 40, 88, 21, 95]
```

### Features

- Total Marks
- Average Marks
- Highest Mark
- Lowest Mark
- Pass Count
- Fail Count

Concepts Used:

- Lists
- Loops
- Conditions
- Counters
- Analytics

---



# 🏢 Real-World AI/ML Connection

Lists are widely used in:

- 🤖 Machine Learning Datasets
- 📊 Data Analysis
- 📈 Customer Analytics
- 🌡️ Sensor Readings
- 📉 Model Predictions
- 🧠 Training Data Processing

Example:

```python
customer_ages = [18, 25, 32, 45, 29]
```

Almost every AI application starts by collecting and processing data stored in lists.

# 🚀 Day 6 — Dictionaries in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-6-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Dictionaries-orange?style=for-the-badge)

### 🔥 Learning to Store and Analyze Structured Data

</div>

---

# 🎯 Goal of Day 6

Today I learned how to work with Python Dictionaries to store, access, update, and analyze structured data.

By the end of today, I can:

✅ Create Dictionaries  
✅ Access Values using Keys  
✅ Add New Data  
✅ Update Existing Data  
✅ Delete Data  
✅ Traverse Dictionaries  
✅ Perform Dictionary Analytics  

---

# 📚 What I Learned Today

## 🔹 Dictionary Basics

A dictionary stores data in:

```text
Key : Value
```

Example:

```python
student = {
    "name": "Siva",
    "age": 21,
    "marks": 92
}
```

---

## 🔹 Accessing Values

```python
student = {
    "name": "Siva",
    "age": 21
}

print(student["name"])
```

Output:

```text
Siva
```

---

## 🔹 Adding New Data

```python
student = {
    "name": "Siva"
}

student["age"] = 21

print(student)
```

Output:

```python
{
    "name": "Siva",
    "age": 21
}
```

---

## 🔹 Updating Existing Data

```python
student = {
    "marks": 92
}

student["marks"] = 97

print(student)
```

Output:

```python
{
    "marks": 97
}
```

---

## 🔹 Removing Data

```python
student = {
    "name": "Siva",
    "age": 21
}

del student["age"]

print(student)
```

Output:

```python
{
    "name": "Siva"
}
```

---

# 🔄 Looping Through Dictionaries

## Printing Keys

```python
for key in student:
    print(key)
```

---

## Printing Values

```python
for key in student:
    print(student[key])
```

---

## Printing Key-Value Pairs

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Siva
age 21
marks 92
```

---

# 💻 Programs Implemented

## Student Dictionary

```python
student = {
    "name": "Siva",
    "age": 21,
    "marks": 92
}
```

---

## Employee Record

```python
employee = {
    "name": "Ravi",
    "salary": 60000,
    "department": "AI"
}
```

---

## Customer Record

```python
customer = {
    "id": 101,
    "name": "Siva Kumar",
    "city": "Guntur",
    "age": 21
}
```

---

# 📊 Dictionary Analytics Mini Project

Dataset:

```python
students = {
    "Siva": 92,
    "Rahul": 78,
    "Priya": 85,
    "Arjun": 35,
    "Kiran": 65
}
```

### Tasks Performed

- Total Marks
- Average Marks
- Highest Mark
- Lowest Mark
- Pass Count
- Fail Count

### Concepts Used

- Dictionaries
- Loops
- Conditions
- Analytics
- Aggregation

---

# 🏢 Real-World AI/ML Connection

Dictionaries are heavily used in:

- 🤖 Machine Learning Pipelines
- 🌐 REST APIs
- 📄 JSON Data
- 📊 Data Analysis
- 🏗️ Data Engineering
- 🧠 AI Applications

Example:

```python
prediction = {
    "customer_id": 101,
    "prediction": "Churn",
    "confidence": 0.95
}
```

Most real-world API responses are dictionary-like JSON objects.

---

# 🧠 Debugging & Interview Concepts

## KeyError Example

```python
student = {
    "name": "Siva"
}

print(student["age"])
```

Output:

```text
KeyError: 'age'
```

Reason:
The key `"age"` does not exist.

---

## Logical Error Example

```python
student = {
    "marks": 92
}

student["marks"] = student["marks"] - 100
```

Output:

```text
-8
```

Python executes successfully, but the business logic is incorrect.

---

# 🧠 Practice Programs Completed

- ✅ Student Dictionary
- ✅ Employee Dictionary
- ✅ Customer Dictionary
- ✅ Add New Keys
- ✅ Update Values
- ✅ Delete Keys
- ✅ Dictionary Traversal
- ✅ Dictionary Analytics
- ✅ Missing Key Debugging

---


```

# 🚀 Day 7 — Tuples in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-7-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Tuples-orange?style=for-the-badge)

### 🔥 Learning Immutable Data Structures for Reliable Data Storage

</div>

---

# 🎯 Goal of Day 7

Today I learned how to work with Python Tuples and understand when immutable collections are useful.

By the end of today, I can:

✅ Create Tuples  
✅ Access Tuple Elements  
✅ Traverse Tuples  
✅ Perform Tuple Analytics  
✅ Understand Immutability  
✅ Solve Data Analysis Problems using Tuples  

---

# 📚 What I Learned Today

## 🔹 Tuple Basics

A tuple is an ordered collection of values that cannot be modified after creation.

```python
student = ("Siva", 21, 92)

print(student)
```

Output:

```text
('Siva', 21, 92)
```

---

## 🔹 Tuple vs List

### List (Mutable)

```python
numbers = [10, 20, 30]

numbers[0] = 100
```

✔ Allowed

### Tuple (Immutable)

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

❌ Error

---

## 🔹 Accessing Tuple Elements

### Positive Indexing

```python
student = ("Siva", 21, 92)

print(student[0])
```

Output:

```text
Siva
```

### Negative Indexing

```python
student = ("Siva", 21, 92)

print(student[-1])
```

Output:

```text
92
```

---

## 🔹 Tuple Traversal

```python
numbers = (5, 10, 15, 20)

for num in numbers:
    print(num)
```

Output:

```text
5
10
15
20
```

---

## 🔹 Length of a Tuple

```python
data = (5, 10, 15)

print(len(data))
```

Output:

```text
3
```

---

# 📊 Tuple Analytics

## Sum of Tuple Values

```python
numbers = (10, 20, 30)

total = 0

for num in numbers:
    total += num

print(total)
```

Output:

```text
60
```

---

## Count Values Greater Than 80

```python
marks = (78, 92, 45, 88)

count = 0

for mark in marks:
    if mark > 80:
        count += 1

print(count)
```

Output:

```text
2
```

---

## Finding Largest Value

```python
marks = (78, 92, 45, 88)

largest = marks[0]

for mark in marks:
    if mark > largest:
        largest = mark

print(largest)
```

Output:

```text
92
```

---

## Finding Smallest Value

```python
marks = (78, 92, 45, 88)

smallest = marks[0]

for mark in marks:
    if mark < smallest:
        smallest = mark

print(smallest)
```

Output:

```text
45
```

---

## Finding Average

```python
marks = (78, 92, 45, 88)

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print(average)
```

---

# 💻 Mini Project — Student Marks Analytics

Dataset:

```python
marks = (65, 78, 92, 35, 40, 88, 21, 95)
```

### Features

- Total Marks
- Average Marks
- Highest Mark
- Lowest Mark
- Pass Count
- Fail Count
- Range Calculation

### Concepts Used

- Tuples
- Loops
- Conditions
- Aggregation
- Analytics

---

# 🏢 Real-World AI/ML Connection

Tuples are used for fixed values that should not change.

### Image Coordinates

```python
position = (120, 250)
```

### Geographic Coordinates

```python
location = (17.3850, 78.4867)
```

### RGB Colors

```python
color = (255, 0, 0)
```

### Machine Learning Data

```python
prediction = ("Customer_101", "Churn", 0.95)
```

Commonly used in:

- 🤖 Machine Learning
- 📊 Data Analysis
- 🖼️ Computer Vision
- 🌍 GIS Systems
- 🎨 Graphics Programming

---

# 🧠 Debugging & Interview Concepts

## Common Bug

Incorrect:

```python
total = num
```

Correct:

```python
total += num
```

Reason:

```text
total = num
```

replaces the value instead of accumulating it.

---

## Largest vs Smallest Logic

Largest:

```python
if value > largest:
    largest = value
```

Smallest:

```python
if value < smallest:
    smallest = value
```

---

## Important Testing Cases

```python
(1, 2, 3, 4)
(4, 3, 2, 1)
(3, 1, 4, 2)
(-5, 10, -2, 7)
```

Never assume one dataset is enough.

---

# 📈 Statistical Concept Introduced

## Range

Formula:

```text
Range = Highest Value - Lowest Value
```

Example:

```python
data = (50, 20, 80, 10)
```

```text
Range = 80 - 10 = 70
```

# 🚀 Day 8 — Sets in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-8-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Sets-orange?style=for-the-badge)

### 🔥 Learning Data Cleaning & Duplicate Detection with Sets

</div>

---

# 🎯 Goal of Day 8

Today I learned how Sets work in Python and how they help remove duplicates, check membership efficiently, and perform data-cleaning tasks used in AI/ML pipelines.

By the end of today, I can:

✅ Create Sets  
✅ Remove Duplicate Values  
✅ Add & Remove Elements  
✅ Perform Membership Testing  
✅ Detect Duplicates  
✅ Analyze Data Quality Metrics  

---

# 📚 What I Learned Today

## 🔹 What is a Set?

A Set is an unordered collection of unique values.

```python
numbers = {10, 20, 30}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

---

## 🔹 Duplicate Removal

Sets automatically remove duplicate values.

```python
data = {10, 20, 10, 30, 20}

print(data)
```

Output:

```text
{10, 20, 30}
```

---

## 🔹 Creating Sets

```python
numbers = {10, 20, 30}

print(numbers)
```

---

## 🔹 Adding Elements

```python
numbers = {10, 20}

numbers.add(30)

print(numbers)
```

Output:

```text
{10, 20, 30}
```

---

## 🔹 Removing Elements

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

Output:

```text
{10, 30}
```

---

## 🔹 Membership Testing

```python
numbers = {10, 20, 30}

if 20 in numbers:
    print("Found")
```

Output:

```text
Found
```

---

## 🔹 Counting Unique Values

```python
data = [10, 20, 10, 30, 20]

print(len(set(data)))
```

Output:

```text
3
```

Unique Values:

```text
10
20
30
```

---

## 🔹 Duplicate Detection

```python
data = [10, 20, 10, 30]

if len(data) != len(set(data)):
    print("Duplicates Found")
else:
    print("No Duplicates")
```

Output:

```text
Duplicates Found
```

---

# 📊 Data Quality Metrics

## Duplicate Count

Formula:

```python
duplicate_count = len(data) - len(set(data))
```

Example:

```python
data = [10, 20, 10, 30, 20, 40]
```

Output:

```text
2 duplicate records
```

---

## Unique Percentage

Formula:

```python
unique_percentage = len(set(data)) / len(data) * 100
```

Example Result:

```text
66.67%
```

Meaning:

```text
66.67% of records are unique
```

---

## Duplicate Percentage

Formula:

```python
duplicate_percentage = duplicate_count / len(data) * 100
```

Example Result:

```text
33.33%
```

---

# 💻 Mini Project — Customer Data Cleaner

Dataset:

```python
customer_ids = [
    101, 102, 101,
    103, 102, 104
]
```

### Features

- Remove Duplicate Customers
- Count Unique Records
- Count Duplicate Records
- Calculate Data Quality Metrics
- Membership Testing

### Concepts Used

- Sets
- Lists
- Conditions
- Analytics
- Data Cleaning

---

# 🏢 Real-World AI/ML Connection

Sets are commonly used in:

### Customer Deduplication

```python
unique_customers = set(customer_ids)
```

### Email Deduplication

```python
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com"
]

unique_emails = set(emails)
```

### Fraud Detection

```python
fraud_users = {
    101,
    102,
    105,
    110
}
```

Check:

```python
if 105 in fraud_users:
    print("Fraud User")
```

Used in:

- 🤖 Machine Learning Preprocessing
- 📊 Data Analysis
- 🧹 Data Cleaning
- 🔍 Fraud Detection
- 📈 Customer Analytics

---

# 🧠 Interview Concepts Learned

## Business Meaning of Output

Instead of asking:

```text
What does this code print?
```

Ask:

```text
What business information does this provide?
```

Example:

```python
len(data) - len(set(data))
```

Meaning:

```text
Number of duplicate records in the dataset
```

---

## Data Quality Analysis

Using:

```python
len(data)
len(set(data))
```

We can determine:

- Total Records
- Unique Records
- Duplicate Records
- Unique Percentage
- Duplicate Percentage

These are common preprocessing tasks before training ML models.

---

# 🧠 Practice Programs Completed

- ✅ Set Creation
- ✅ add()
- ✅ remove()
- ✅ Membership Testing
- ✅ Duplicate Detection
- ✅ Unique Record Counting
- ✅ Duplicate Record Counting
- ✅ Customer Data Cleaning
- ✅ Email Deduplication
- ✅ Fraud User Detection
- ✅ Data Quality Metrics

# 🚀 Day 9 — Strings in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-9-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Strings-orange?style=for-the-badge)

### 🔥 Learning Text Processing for AI, NLP & Data Cleaning

</div>

---

# 🎯 Goal of Day 9

Today I learned how to work with strings in Python and perform text processing tasks used in AI, Machine Learning, and Data Analysis.

By the end of today, I can:

✅ Create Strings  
✅ Access Characters using Indexing  
✅ Traverse Strings  
✅ Use String Slicing  
✅ Apply String Methods  
✅ Perform Text Cleaning  
✅ Solve String-Based Problems

---

# 📚 What I Learned Today

## 🔹 What is a String?

A string is a sequence of characters.

```python
name = "Siva"

print(name)
```

Output:

```text
Siva
```

---

## 🔹 String Indexing

Every character has an index.

| Character | S | i | v | a |
|-----------|---|---|---|---|
| Index | 0 | 1 | 2 | 3 |

### First Character

```python
print(name[0])
```

Output:

```text
S
```

### Last Character

```python
print(name[-1])
```

Output:

```text
a
```

---

## 🔹 Length of a String

```python
name = "Siva"

print(len(name))
```

Output:

```text
4
```

---

## 🔹 Traversing a String

```python
text = "AI"

for ch in text:
    print(ch)
```

Output:

```text
A
I
```

---

## 🔹 String Slicing

Syntax:

```python
text[start:end]
```

Rule:

```text
Start Index → Included
End Index → Excluded
```

Example:

```python
text = "Machine"

print(text[0:3])
```

Output:

```text
Mac
```

### Last Three Characters

```python
print(text[-3:])
```

Output:

```text
ine
```

---

# 🛠️ String Methods

## upper()

```python
name = "siva"

print(name.upper())
```

Output:

```text
SIVA
```

---

## lower()

```python
name = "SIVA"

print(name.lower())
```

Output:

```text
siva
```

---

## replace()

```python
text = "Data Science"

print(text.replace("Science", "Engineering"))
```

Output:

```text
Data Engineering
```

---

## count()

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

## strip()

```python
name = "  Siva  "

print(name.strip())
```

Output:

```text
Siva
```

---

# 💻 Problems Solved

## Character Counting

```python
review = "Amazing"

count = 0

for ch in review:
    count += 1

print(count)
```

Output:

```text
7
```

---

## Lowercase Conversion

```python
reviews = [
    "GOOD",
    "Excellent",
    "BAD",
    "Amazing"
]

for review in reviews:
    print(review.lower())
```

---

## Text Replacement

```python
text = "Data Science"

print(text.replace("Science", "Engineering"))
```

Output:

```text
Data Engineering
```

---

# 🏢 Real-World AI/ML Connection

Strings are everywhere in AI and Machine Learning:

### Text Normalization

```python
review = "GOOD PRODUCT"

print(review.lower())
```

Output:

```text
good product
```

---

### Data Cleaning

```python
name = "  Siva  "

print(name.strip())
```

---

### Email Validation

```python
email = "siva@gmail.com"

if "@" in email:
    print("Valid Email")
```

---

### NLP & Chat Applications

Examples:

- Customer Reviews
- Chat Messages
- Emails
- Documents
- AI Prompts
- Chatbots

---

# 🧠 Important Concepts Learned

## Concatenation

```python
print("AI" + "ML")
```

Output:

```text
AIML
```

---

## String Repetition

```python
print("AI" * 3)
```

Output:

```text
AIAIAI
```

---

## Membership Testing

```python
email = "siva@gmail.com"

print("@" in email)
```

Output:

```text
True
```

---

# 🏢 Interview Questions Practiced

## Question 1

```python
text = "AI"

print(text[0] + text[1])
```

Output:

```text
AI
```

Concept:

```text
String Concatenation
```

---

## Question 2

```python
print("AI" * 3)
```

Output:

```text
AIAIAI
```

Concept:

```text
String Repetition
```

---

## Question 3

```python
text = "Python"

print(text[1:5])
```

Output:

```text
ytho
```

Concept:

```text
String Slicing
```


<div align="center">

## ⭐ Day 9 Completed Successfully

### 🚀 Building Strong Foundations for AI, NLP & Machine Learning

</div>

# 🚀 Day 10 — Advanced Strings in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge&logo=python)
![Day](https://img.shields.io/badge/Day-10-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Advanced%20Strings-orange?style=for-the-badge)

### 🔥 Learning Text Processing for NLP, AI & Machine Learning

</div>

---

# 🎯 Goal of Day 10

Today I learned advanced string operations used in AI, Machine Learning, NLP, and real-world Python applications.

By the end of today, I can:

✅ Use Advanced String Operations  
✅ Reverse Strings Efficiently  
✅ Perform Text Cleaning  
✅ Solve Interview String Problems  
✅ Build Validation Systems  
✅ Prepare Text for NLP Applications  

---

# 📚 What I Learned Today

## 🔹 String Indexing

```python
text = "Python"

print(text[0])
print(text[-1])
```

Output:

```text
P
n
```

---

## 🔹 String Slicing

```python
text = "MachineLearning"

print(text[0:7])
print(text[7:])
print(text[:7])
```

Output:

```text
Machine
Learning
Machine
```

---

## 🔹 Step Slicing

```python
text = "Python"

print(text[::2])
```

Output:

```text
Pto
```

---

## 🔹 Reverse a String

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

---

# 🛠️ Advanced String Methods

## lower()

```python
print("HELLO".lower())
```

Output:

```text
hello
```

---

## upper()

```python
print("python".upper())
```

Output:

```text
PYTHON
```

---

## strip()

```python
print("  Python  ".strip())
```

Output:

```text
Python
```

---

## replace()

```python
print("I like Java".replace("Java", "Python"))
```

Output:

```text
I like Python
```

---

## split()

```python
print("AI,ML,DL".split(","))
```

Output:

```text
['AI', 'ML', 'DL']
```

---

## count()

```python
print("banana".count("a"))
```

Output:

```text
3
```

---

## find()

```python
print("Machine".find("i"))
```

Output:

```text
4
```

---

## startswith() & endswith()

```python
print("siva@gmail.com".startswith("siva"))
print("resume.pdf".endswith(".pdf"))
```

Output:

```text
True
True
```

---

# 💻 Interview Problems Solved

## Palindrome Check

```python
word = "level"

if word == word[::-1]:
    print("Palindrome")
```

---

## Character Frequency Counter

```python
text = "Python"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

Output:

```python
{'P':1,'y':1,'t':1,'h':1,'o':1,'n':1}
```

---

## Longest Word Finder

```python
text = "Artificial Intelligence Engineer"

words = text.split()

print(max(words, key=len))
```

Output:

```text
Intelligence
```

---

## First Non-Repeating Character

```python
text = "aabbccdeeff"

for ch in text:
    if text.count(ch) == 1:
        print(ch)
        break
```

Output:

```text
d
```

---

## Anagram Check

```python
a = "earth"
b = "heart"

if sorted(a) == sorted(b):
    print("Anagram")
```

Output:

```text
Anagram
```

---

# 🏢 Real-World AI/ML Connection

### Text Cleaning

```python
reviews = [
    " GREAT ",
    "Excellent",
    " bad "
]

for review in reviews:
    print(review.strip().lower())
```

Output:

```text
great
excellent
bad
```

Used in:

- 🤖 NLP Pipelines
- 💬 Chatbots
- 📊 Sentiment Analysis
- 📄 Resume Parsing
- 🧠 LLM Applications

---

# 🚀 Mini Projects

## Email Validator

```python
email = "siva@gmail.com"

if "@" in email and email.endswith(".com"):
    print("Valid Email")
```

---

## Username Generator

```python
name = "Machine Learning Engineer"

print(name.lower().replace(" ", "_"))
```

Output:

```text
machine_learning_engineer
```

---

## Password Strength Checker

```python
password = "AI2026ML"

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Strong Password")
```

---

## Word Counter

```python
text = "Artificial Intelligence Engineer"

print(len(text.split()))
```

Output:

```text
3
```
# 🚀 Day 11: File Handling for Data Scientists

## 📅 Day 11 of AI/Data Scientist Roadmap

## 🎯 Objective

Learn how to:

- Read files
- Write files
- Append data
- Work with CSV files
- Process datasets
- Build real-world data handling applications

---

# 📚 Topics Covered

## 1. Reading Files

### read()

Reads the entire file.

```python
with open("AI.txt", "r") as file:
    content = file.read()
    print(content)
```

---

### readline()

Reads only one line.

```python
with open("AI.txt", "r") as file:
    print(file.readline())
```

---

### readlines()

Returns all lines as a list.

```python
with open("AI.txt", "r") as file:
    print(file.readlines())
```

Output:

```python
['Python\n', 'ML\n', 'AI\n']
```

---

## 2. Using with open()

Industry-standard approach.

```python
with open("AI.txt", "r") as file:
    content = file.read()
```

### Benefits

✅ Automatically closes files

✅ Prevents resource leaks

✅ Cleaner code

✅ Used in production systems

---

# 💼 Real-World Scenario

Reading customer reviews before sentiment analysis.

```python
with open("reviews.txt", "r") as file:
    reviews = file.read()
```

---

# ✍️ Writing Files

## Write Mode (w)

```python
with open("student.txt", "w") as file:
    file.write("Siva")
```

### Important

```text
Old content is deleted.
New content is written.
```

---

## Writing Multiple Lines

```python
with open("skills.txt", "w") as file:

    file.write("Python\n")
    file.write("SQL\n")
    file.write("Machine Learning\n")
```

Output:

```text
Python
SQL
Machine Learning
```

---

# 📌 Append Mode (a)

Append adds new data without removing old content.

```python
with open("skills.txt", "a") as file:
    file.write("Deep Learning\n")
```

---

## Difference Between w and a

| Mode | Behavior |
|--------|----------|
| w | Deletes old content and writes new content |
| a | Keeps old content and adds new content |

---

# 📊 Logging System

Logs are used everywhere in software and ML systems.

```python
with open("log.txt", "a") as file:
    file.write("User Logged In\n")
```

Example Log File:

```text
User Logged In
User Purchased Product
Payment Success
```

---

# 📁 CSV Files

CSV = Comma Separated Values

Example:

```csv
Name,Age
Siva,21
Ravi,22
Anjali,20
```

---

## Import CSV Module

```python
import csv
```

---

## Read CSV File

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```python
['Name', 'Age']
['Siva', '21']
['Ravi', '22']
```

---

## Skip Header

```python
next(reader)
```

---

## Access Individual Columns

```python
print(row[0])  # Name

print(row[1])  # Age
```

---

## Write CSV File

```python
import csv

with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Salary"])

    writer.writerow(["Siva", 50000])

    writer.writerow(["Ravi", 45000])
```

Output:

```csv
Name,Salary
Siva,50000
Ravi,45000
```

---

# 💼 Real ML Applications

## Sentiment Analysis Dataset

```csv
Review,Label
Amazing Product,Positive
Bad Service,Negative
Excellent Product,Positive
```

Read Labels:

```python
import csv

with open("reviews.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row[1])
```

Output:

```text
Positive
Negative
Positive
```

---

# 🏆 Mini Projects

## Employee Log System

```python
with open("employee_log.txt", "a") as file:

    file.write("Siva Logged In\n")
    file.write("Ravi Logged In\n")
    file.write("Kumar Logged In\n")
```

---

## Student CSV Analyzer

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    count = 0

    for row in reader:
        print(row[0])
        count += 1

print(f"Total Students: {count}")
```


# 🚀 Day 12 — Exception Handling in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-12-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Exception%20Handling-orange?style=for-the-badge)

### 🔥 Building Robust & Error-Free Python Applications

</div>

---

# 🎯 Goal of Day 12

Today I learned how to write robust Python programs that can handle unexpected errors without crashing.

By the end of today, I can:

✅ Handle Runtime Exceptions
✅ Prevent Program Crashes
✅ Write Production-Ready Code
✅ Debug Common Python Errors
✅ Build Reliable Applications

---

# 📚 What I Learned Today

## 🔹 What is an Exception?

An exception is an error that occurs while a program is running.

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

---

## 🔹 try & except

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 🔹 ValueError

```python
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid number.")
```

---

## 🔹 ZeroDivisionError

```python
try:
    result = 100 / 0

except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

## 🔹 FileNotFoundError

```python
try:
    with open("AI.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")
```

---

## 🔹 else Block

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input")

else:
    print("Valid input")
```

---

## 🔹 finally Block

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Program Finished")
```

---

## 🔹 Common Python Exceptions

### IndexError

```python
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist.")
```

### KeyError

```python
student = {
    "name": "Siva"
}

try:
    print(student["marks"])

except KeyError:
    print("Key not found.")
```

### TypeError

```python
try:
    print(10 + "20")

except TypeError:
    print("Cannot add integer and string.")
```

### NameError

```python
try:
    print(total_marks)

except NameError:
    print("Variable is not defined.")
```

### AttributeError

```python
try:
    number = 100
    number.append(10)

except AttributeError:
    print("Method not available for this object.")
```

---

# 💻 Mini Projects

## Safe Marks Calculator

* Accept user input
* Handle invalid values
* Prevent division by zero
* Calculate average safely

---

## Safe Dataset Loader

* Load a dataset from a file
* Handle missing files
* Display success or error messages
* Always complete cleanup using `finally`

# 🚀 Day 13 — Object-Oriented Programming (OOP) in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-13-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Object--Oriented%20Programming-orange?style=for-the-badge)

### 🔥 Building Scalable Python Applications with OOP

</div>

---

# 🎯 Goal of Day 13

Today I learned how to organize Python code using Object-Oriented Programming (OOP).

By the end of today, I can:

✅ Create Classes and Objects
✅ Use Constructors (`__init__`)
✅ Understand `self`
✅ Work with Instance & Class Variables
✅ Write Reusable Methods
✅ Build Real-World OOP Applications

---

# 📚 What I Learned Today

## 🔹 Classes & Objects

A class is a blueprint for creating objects.

```python
class Student:
    pass

student1 = Student()
```

---

## 🔹 Constructors (`__init__`)

Initialize object data automatically.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 🔹 Understanding `self`

`self` refers to the current object.

```python
class Student:

    def display(self):
        print(self.name)
```

---

## 🔹 Instance Variables

Each object stores its own data.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## 🔹 Class Variables

Shared among all objects.

```python
class Student:

    college = "ABC University"
```

---

## 🔹 Instance Methods

Methods define an object's behavior.

```python
class Student:

    def greet(self):
        print("Welcome", self.name)
```

---

## 🔹 `__str__()` Method

Provides a readable string representation of an object.

```python
class Student:

    def __str__(self):
        return self.name
```

---

# 💻 Coding Practice

Implemented multiple OOP programs:

* ✅ Student Management System
* ✅ Employee Management System
* ✅ Bank Account System
* ✅ Library Management System
* ✅ Online Course Management System

---

# 🏗️ Mini Projects

## 📖 Library Management System

Features:

* Store book details
* Borrow books
* Return books
* Validate availability

---

## 🎓 Online Course Management System

Features:

* Add course details
* Enroll students
* Update available seats
* Manage course information

---

# 🏢 Real-World AI/ML Connection

Object-Oriented Programming is used in:

* 🤖 Machine Learning Libraries
* 📊 Data Processing Pipelines
* 🌐 Web Applications
* 🏦 Banking Systems
* 🏥 Hospital Management
* 🛒 E-commerce Platforms

Libraries such as **TensorFlow**, **PyTorch**, and **Scikit-learn** are heavily built using OOP concepts.


# 🚀 Day 14 – Advanced Object-Oriented Programming (OOP) in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-14-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Advanced%20OOP-orange?style=for-the-badge)

### 🔥 Writing Cleaner, Reusable, and Better Python Programs

</div>

---

# 🎯 Goal of Day 14

Today I learned how to organize data and methods more effectively using Advanced Object-Oriented Programming concepts.

By the end of today, I can:

* ✅ Differentiate between Instance Variables and Class Variables
* ✅ Decide when to use Instance Methods, Class Methods, and Static Methods
* ✅ Avoid duplicate data using Class Variables
* ✅ Write cleaner and more maintainable Python code
* ✅ Apply OOP concepts to real-world applications

---

# 📚 Topics Covered

## 🔹 Class Variables

A class variable is shared by all objects of a class. It is useful when every object has the same information.

### Example

```python
class Student:

    school_name = "ABC Public School"

    def __init__(self, name):
        self.name = name
```

---

## 🔹 Instance Variables vs Class Variables

### Instance Variables

* Belong to individual objects
* Each object has its own copy

Examples:

* Name
* Roll Number
* Marks

### Class Variables

* Shared by all objects
* Stored only once inside the class

Examples:

* School Name
* Company Name
* Country

---

## 🔹 Instance Methods

Instance methods work with the data of a particular object using `self`.

### Example

```python
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

---

## 🔹 Class Methods

Class methods work with class-level data using `cls`.

### Example

```python
class Student:

    school_name = "ABC Public School"

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
```

---

## 🔹 Static Methods

Static methods perform helper tasks that don't require object data or class data.

### Example

```python
class Citizen:

    @staticmethod
    def is_eligible(age):
        return age >= 18
```

---

# 💻 Practice Programs Completed

* ✅ Student Management System (Class Variable)
* ✅ Employee Management System (Class Method)
* ✅ Library Management System (Instance Method)
* ✅ School Name Updater (Class Method)
* ✅ Voting Eligibility Checker (Static Method)

---

# 🌍 Real-World Applications

These OOP concepts are widely used in:

* 🏫 Student Management Systems
* 🏢 Employee Management Systems
* 🏦 Banking Applications
* 📚 Library Management Systems
* 🛒 E-commerce Applications
* 📱 Desktop and Web Applications

# 🚀 Day 15 – Inheritance in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-15-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Inheritance-orange?style=for-the-badge)

### 🔥 Reusing Code with Object-Oriented Programming

</div>

---

# 🎯 Goal of Day 15

Today I learned one of the most important concepts in Object-Oriented Programming: **Inheritance**.

Inheritance allows one class to reuse the properties and methods of another class, reducing duplicate code and making programs easier to maintain.

By the end of today, I can:

* ✅ Create Parent and Child classes
* ✅ Reuse code using Inheritance
* ✅ Use the `super()` function correctly
* ✅ Extend a Parent class with new attributes and methods
* ✅ Solve inheritance-based coding problems
* ✅ Understand how inheritance is used in real-world software

---

# 📚 Topics Covered

## 🔹 What is Inheritance?

Inheritance allows a child class to reuse the attributes and methods of a parent class.

### Example

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass
```

---

## 🔹 Parent Class

A parent class contains common properties and behaviors that can be shared with other classes.

Example:

* Person
* Vehicle
* Animal
* Product

---

## 🔹 Child Class

A child class inherits from the parent class and can also have its own attributes and methods.

Example:

* Student
* Teacher
* Car
* Dog

---

## 🔹 Using `super()`

The `super()` function calls the parent class constructor or methods, allowing the child class to reuse existing code.

### Example

```python
class Student(Person):

    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
```

---

## 🔹 Adding New Features

A child class can inherit everything from the parent class while adding its own data and functionality.

Example:

* Person → Name, Age
* Student → Roll Number
* Teacher → Subject

---

# 💻 Practice Programs Completed

* ✅ Person → Student
* ✅ Person → Teacher
* ✅ Vehicle → Car
* ✅ Animal → Dog
* ✅ Animal → Cat
* ✅ BankAccount → SavingsAccount
* ✅ Product → Electronics
* ✅ Product → Clothing
* ✅ Hospital Management System
* ✅ Employee Management System

# 🚀 Day 16 – Types of Inheritance, Method Overriding, `super()` & MRO

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-16-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Advanced%20OOP-orange?style=for-the-badge)

### 🔥 Building Flexible and Reusable Object-Oriented Programs

</div>

---

# 🎯 Goal of Day 16

Today I explored advanced Object-Oriented Programming concepts by learning different types of inheritance, method overriding, the `super()` function, and Method Resolution Order (MRO).

By the end of today, I can:

* ✅ Identify different inheritance types
* ✅ Choose the correct inheritance structure for a problem
* ✅ Override parent methods in child classes
* ✅ Use `super()` in constructors and normal methods
* ✅ Understand how Python resolves methods using MRO
* ✅ Solve inheritance-based company coding questions

---

# 📚 Topics Covered

## 🔹 Types of Inheritance

Python supports multiple ways of sharing code between classes.

### Single Inheritance

One child class inherits from one parent class.

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

---

### Multilevel Inheritance

A child class becomes the parent of another class.

```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass
```

---

### Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

```python
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass
```

---

### Multiple Inheritance

One child class inherits from multiple parent classes.

```python
class Camera:
    pass

class Phone:
    pass

class SmartPhone(Camera, Phone):
    pass
```

---

### Hybrid Inheritance

Hybrid inheritance combines two or more inheritance types to model more complex relationships.

---

# 🔹 Method Overriding

Method overriding allows a child class to provide its own implementation of a method already defined in the parent class.

### Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")
```

---

# 🔹 Using `super()`

The `super()` function is used to call methods or constructors from the parent class.

### Constructor Example

```python
class Student(Person):

    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
```

---

### Method Example

```python
class Car(Vehicle):

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
```

Using `super()` helps avoid duplicate code and keeps programs easier to maintain.

---

# 🔹 Method Resolution Order (MRO)

When multiple inheritance is used, Python follows a specific order to decide which method should be executed.

### Example

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
```

MRO ensures that Python always knows which method to execute first when multiple parent classes contain methods with the same name.

---

# 💻 Practice Programs Completed

* ✅ Single Inheritance Examples
* ✅ Multilevel Inheritance Examples
* ✅ Hierarchical Inheritance Examples
* ✅ Multiple Inheritance Examples
* ✅ Method Overriding Practice
* ✅ `super()` with Constructors
* ✅ `super()` with Methods
* ✅ MRO Demonstration
* ✅ Banking System
* ✅ Vehicle Management System
* ✅ University Management System

# 🚀 Day 17 – Polymorphism, Duck Typing & Operator Overloading

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced_OOP-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-17-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Polymorphism-orange?style=for-the-badge)

### 🔥 Learning Advanced Object-Oriented Programming in Python

</div>

---

# 🎯 Goal of Day 17

Today I learned advanced Object-Oriented Programming concepts that make software more flexible, scalable, and maintainable.

By the end of today, I can:

* ✅ Explain Polymorphism
* ✅ Differentiate Runtime and Compile-Time Polymorphism
* ✅ Apply Method Overriding
* ✅ Understand Duck Typing
* ✅ Perform Operator Overloading
* ✅ Use Magic (Dunder) Methods
* ✅ Explain Built-in Polymorphism
* ✅ Solve company-style OOP coding problems

---

# 📚 Topics Covered

## 🔹 Polymorphism

Polymorphism means **"many forms."**

It allows the same method to perform different actions depending on the object that calls it.

### Runtime Polymorphism

Achieved using **Method Overriding**.

```python
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog: Bark")

class Cat(Animal):
    def make_sound(self):
        print("Cat: Meow")
```

---

### Compile-Time Polymorphism

Python does not support traditional method overloading like Java or C++.

Instead, similar behavior can be achieved using:

* Default Arguments
* `*args`
* `**kwargs`

---

## 🔹 Duck Typing

Python focuses on **object behavior rather than object type**.

If an object implements the required method, it can be used.

### Example

```python
class Dog:
    def speak(self):
        print("Woof")

class Person:
    def speak(self):
        print("Hello")

def talk(obj):
    obj.speak()

talk(Dog())
talk(Person())
```

---

## 🔹 Operator Overloading

Python allows developers to redefine how operators behave for custom classes.

### Example

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
```

This allows:

```python
n1 + n2
```

instead of manually calling another method.

---

## 🔹 Magic (Dunder) Methods

Learned commonly used magic methods:

* `__init__()`
* `__str__()`
* `__repr__()`
* `__len__()`
* `__add__()`
* `__sub__()`
* `__mul__()`
* `__eq__()`

These methods define how Python interacts with custom objects.

---

## 🔹 Built-in Polymorphism

Python's built-in functions work with multiple object types.

Examples:

```python
len("Python")
len([1, 2, 3])
len({"A": 1})
```

The same function behaves differently depending on the object.

---

# 💻 Company-Style Coding Practice

Solved interview-oriented coding problems based on:

* ✅ Animal Sound System
* ✅ Notification Management System
* ✅ Banking Interest Calculation
* ✅ Shape Area Calculator
* ✅ Ride Booking System
* ✅ Employee Payroll System
* ✅ Shopping Cart System
* ✅ Operator Overloading
* ✅ Debugging OOP Programs

---

# 🏢 Real-World Applications

These concepts are widely used in:

* 💳 Payment Gateways
* 📧 Notification Services
* 🛒 E-commerce Platforms
* 🏦 Banking Applications
* 🚕 Ride-Sharing Systems
* 🎮 Game Development
* 📦 Inventory Management
* 📊 Data Processing Libraries
* 🤖 AI and Machine Learning Frameworks

---

# 🔗 Data Science & Generative AI Connection

These OOP concepts are heavily used in Data Science and AI libraries.

### Scikit-learn

Machine learning models expose a common interface:

```python
model.fit(X, y)
model.predict(X)
```

This allows different algorithms to be used with the same workflow.

---

### Pandas

`DataFrame` is an object with methods such as:

```python
df.head()
df.describe()
df.info()
```

---

### NumPy

Operators such as:

```python
array1 + array2
```

work because NumPy overloads operators internally.

---

### Generative AI

Modern AI frameworks expose similar interfaces for different models, making it easier to swap implementations while keeping application code unchanged.

---

# 🧠 Key Takeaways

* Polymorphism enables one interface with multiple implementations.
* Runtime Polymorphism is achieved using Method Overriding.
* Python uses Duck Typing to focus on object behavior instead of object type.
* Operator Overloading makes custom classes behave like built-in types.
* Magic Methods define object behavior inside Python.
* Built-in functions demonstrate polymorphism naturally.
* Good OOP design reduces code duplication and improves scalability.

---

# 📈 Skills Gained

After completing Day 17, I can:

* Design flexible class hierarchies.
* Apply runtime polymorphism.
* Use method overriding confidently.
* Implement Duck Typing.
* Overload operators using magic methods.
* Explain built-in polymorphism.
* Solve company-style OOP problems.
* Understand how advanced OOP concepts are used in Data Science and AI.

---

# 🚀 Mini Project

## Smart Notification Management System

Built a notification system supporting multiple notification channels using polymorphism.

Features:

* Email Notifications
* SMS Notifications
* WhatsApp Notifications
* Common Notification Interface
* Extensible Design

Future enhancements:

* Telegram Notifications
* Slack Notifications
* Push Notifications
* Notification Logging
* Retry Mechanism

---

# 🎯 Next Step

In **Day 18**, I will learn:

* Abstraction
* Abstract Classes
* Abstract Methods
* `abc` Module
* Interfaces in Python
* Real-world System Design using Abstraction

I will also solve company-style coding problems and build another industry-oriented project.

---

# 📌 Day 17 Status

**Completed Successfully ✅**
# 🚀 Day 18 – Abstraction, Abstract Classes & Abstract Methods

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced_OOP-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-18-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Abstraction-orange?style=for-the-badge)

### 🔥 Learning Abstraction in Python Using Real-World and Industry Examples

</div>

---

# 🎯 Goal of Day 18

Today I learned one of the four pillars of Object-Oriented Programming (OOP): **Abstraction**.

The objective was to understand how abstraction hides implementation details while exposing only the required functionality.

By the end of today, I can:

* ✅ Explain Abstraction
* ✅ Understand Abstract Classes
* ✅ Create Abstract Methods
* ✅ Use Python's `abc` module
* ✅ Design reusable software using abstraction
* ✅ Implement child classes that follow a common contract
* ✅ Solve company-style abstraction problems

---

# 📚 Topics Covered

## 🔹 What is Abstraction?

Abstraction is the process of **hiding implementation details** and exposing only the essential functionality.

### Simple Definition

> Show **what** an object can do, but hide **how** it does it.

---

## 🔹 Why Do We Need Abstraction?

Without abstraction:

* Applications become difficult to maintain.
* Users interact with unnecessary implementation details.
* Code becomes tightly coupled.
* Scaling the application becomes harder.

With abstraction:

* Complexity is reduced.
* Code becomes reusable.
* Applications become easier to maintain.
* New features can be added with minimal changes.

---

## 🔹 Real-World Examples

### 🏧 ATM Machine

Visible:

* Insert Card
* Enter PIN
* Withdraw Cash

Hidden:

* PIN Verification
* Server Communication
* Security Checks
* Cash Dispensing Logic

---

### 🚗 Car

Visible:

* Steering
* Brake
* Accelerator

Hidden:

* Engine Control
* Fuel Injection
* Gear Synchronization
* Internal Sensors

---

### 📺 Television Remote

Visible:

* Power Button
* Volume Control

Hidden:

* Circuit Activation
* Operating System Startup
* Display Initialization

---

# 🔹 Abstract Classes

An **Abstract Class** acts as a blueprint for other classes.

Characteristics:

* Cannot be used directly once it contains abstract methods.
* Can contain normal methods.
* Can contain abstract methods.
* Can contain constructors and variables.
* Promotes consistency across child classes.

---

# 🔹 Abstract Methods

Abstract methods define **what every child class must implement**.

Each child class provides its own implementation.

Example concept:

```text
Vehicle
   │
   ├── Car
   ├── Bike
   ├── Truck
   └── ElectricCar
```

Every vehicle must implement:

* `start()`
* `stop()`

---

# 🔹 Python `abc` Module

Learned:

* `ABC`
* `@abstractmethod`

Purpose:

* Create abstract classes.
* Force child classes to implement required methods.
* Prevent incomplete implementations.

---

# 💻 Coding Practice Completed

Completed hands-on exercises covering:

* ✅ Creating Abstract Classes
* ✅ Creating Abstract Methods
* ✅ Implementing Child Classes
* ✅ Object Creation Rules
* ✅ Vehicle Management System
* ✅ Payment System
* ✅ Employee System
* ✅ Bike, Truck and Electric Car Implementation
* ✅ Understanding Python `TypeError` for incomplete subclasses

---

# 🏢 Company-Style Coding Practice

Solved interview-oriented abstraction problems based on:

* Vehicle Management System
* Payment Processing System
* Employee Management System
* Media Player Design
* Machine Learning Model Interface

Focused on:

* Abstraction
* Inheritance
* Method Overriding
* Clean OOP Design

---

# 🌍 Real-World Applications

Abstraction is widely used in:

* 💳 Payment Gateways
* 🚗 Vehicle Management Systems
* 🏥 Hospital Management Systems
* 🎓 University Management Systems
* 🏦 Banking Applications
* 📦 Logistics Platforms
* ☁️ Cloud Services

---

# 🤖 Data Science & Generative AI Connection

Abstraction is heavily used in AI and Data Science libraries.

### Scikit-learn

Different machine learning models expose the same interface:

* `fit()`
* `predict()`

This allows algorithms to be used interchangeably.

---

### TensorFlow & PyTorch

Neural network layers and models follow common interfaces while hiding complex implementation details.

---

### Generative AI

Applications can interact with different language models through a common interface while hiding provider-specific implementation details.

---

# 🧠 Key Takeaways

* Abstraction hides implementation details.
* Abstract Classes provide a common blueprint.
* Abstract Methods enforce a common contract.
* Child classes must implement abstract methods.
* Python uses the `abc` module for abstraction.
* Abstraction improves scalability and maintainability.
* Enterprise software relies heavily on abstraction.

---

# 📈 Skills Gained

After completing Day 18, I can:

* Design software using abstraction.
* Create Abstract Base Classes.
* Define and implement abstract methods.
* Understand object creation rules.
* Build reusable OOP architectures.
* Apply abstraction to real-world software design.
* Explain how abstraction is used in Data Science and Generative AI frameworks.

---

# 🚀 Mini Project

## Smart Vehicle Management System (Version 1)

### Features

* Abstract `Vehicle` class
* Child classes:

  * Car
  * Bike
  * Truck
  * ElectricCar
* Common interface using abstract methods
* Runtime polymorphism
* Clean and extensible architecture

### Future Enhancements

* Bus
* Auto
* Bicycle
* Vehicle Registration
* Vehicle Tracking
* Maintenance Records

---

# 🎯 Next Step

In **Day 19**, I will learn:

* Encapsulation
* Access Modifiers
* Public Members
* Protected Members
* Private Members
* Name Mangling
* Getters & Setters
* `@property` Decorator

I will continue extending the Smart Vehicle Management System while following enterprise-level coding practices.

---

# 📌 Day 18 Status

**Completed Successfully ✅**

# 🚀 Day 19 – Encapsulation, Access Modifiers, Getters, Setters & `@property`

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced_OOP-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-19-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Encapsulation-orange?style=for-the-badge)

### 🔥 Protecting Data and Building Secure Object-Oriented Applications

</div>

---

# 🎯 Goal of Day 19

Today I learned the fourth pillar of Object-Oriented Programming (OOP): **Encapsulation**.

The objective was to understand how to protect an object's internal data by controlling access through methods instead of allowing direct modification.

By the end of today, I can:

* ✅ Explain Encapsulation
* ✅ Differentiate Public, Protected and Private members
* ✅ Understand Name Mangling
* ✅ Create Getter and Setter methods
* ✅ Use the `@property` decorator
* ✅ Design secure and maintainable classes
* ✅ Apply encapsulation in real-world applications

---

# 📚 Topics Covered

## 🔹 What is Encapsulation?

Encapsulation is the process of **binding data (variables) and methods (functions) together inside a class while controlling access to the data**.

### Simple Definition

> Protect an object's data by exposing only controlled methods for accessing and modifying it.

---

## 🔹 Why Do We Need Encapsulation?

Without encapsulation:

* Anyone can modify important data.
* Invalid values can enter the system.
* Security risks increase.
* Applications become difficult to maintain.

With encapsulation:

* Data remains protected.
* Validation becomes possible.
* Code becomes easier to maintain.
* Business rules are enforced consistently.

---

# 🌍 Real-World Examples

## 🏦 Bank Account

Users cannot directly change:

* Account Balance
* ATM PIN

Instead, they use:

* Deposit
* Withdraw
* Check Balance

The application validates every operation.

---

## 📱 Instagram

Users cannot directly modify:

* Followers Count
* Following Count

Instead, Instagram provides:

* Follow
* Unfollow

The application updates the data internally.

---

## 🏥 Hospital Management

Sensitive patient information is protected.

Doctors and staff interact with the system using approved operations such as:

* Update Diagnosis
* Add Prescription
* View Medical History

---

# 🔹 Public Members

Public members are accessible from anywhere.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Public members require no special notation.

---

# 🔹 Protected Members

Protected members begin with a single underscore (`_`).

Example:

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary
```

Protected members are intended for use within the class and its subclasses.

Although Python allows external access, the underscore signals that they are for internal use.

---

# 🔹 Private Members

Private members begin with a double underscore (`__`).

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

Private members are protected using **Name Mangling**, discouraging direct external access.

---

# 🔹 Name Mangling

Python internally changes:

```text
__balance
```

into something similar to:

```text
_BankAccount__balance
```

This makes accidental direct access much more difficult.

---

# 🔹 Getter Methods

Getter methods safely return private data.

Example:

```python
def get_balance(self):
    return self.__balance
```

Benefits:

* Controlled access
* Read-only behavior when needed
* Better maintainability

---

# 🔹 Setter Methods

Setter methods safely update private data after validation.

Example:

```python
def set_salary(self, salary):

    if salary > 0:
        self.__salary = salary
```

Benefits:

* Validation
* Data integrity
* Business rule enforcement

---

# 🔹 `@property` Decorator

The `@property` decorator allows methods to behave like attributes.

Example:

```python
@property
def salary(self):
    return self.__salary
```

Usage:

```python
print(employee.salary)
```

instead of

```python
print(employee.get_salary())
```

This results in cleaner and more Pythonic code.

---

# 💻 Coding Practice Completed

Implemented programs for:

* ✅ Public Members
* ✅ Protected Members
* ✅ Private Members
* ✅ Name Mangling
* ✅ Getter Methods
* ✅ Setter Methods
* ✅ `@property`
* ✅ Student Management
* ✅ Employee Management
* ✅ Product Management
* ✅ Laptop Price Validation

---

# 🏢 Company-Style Coding Practice

Solved interview-oriented coding problems based on:

* Employee Payroll System
* Banking System
* Vehicle Management
* AI Model Management
* Encapsulation with Validation

Focused on:

* Data Protection
* Validation
* Reusability
* Clean OOP Design

---

# 🚀 Enterprise Project

## Smart Vehicle Management System (Version 2)

### Features Added

* Private vehicle information
* Getter methods
* Setter methods
* Price validation
* Secure data handling
* Improved object-oriented design

### OOP Concepts Used

* Encapsulation
* Inheritance
* Abstraction
* Polymorphism

---

# 🌍 Real-World Applications

Encapsulation is widely used in:

* 🏦 Banking Applications
* 🏥 Hospital Management Systems
* 🛒 E-commerce Platforms
* 🚗 Vehicle Management Systems
* 🎓 Student Information Systems
* ☁️ Enterprise Software

---

# 🤖 Data Science & Generative AI Connection

Encapsulation is important in Data Science and AI because many libraries hide complex internal logic while exposing clean APIs.

Examples include:

* Machine Learning model classes
* Data preprocessing pipelines
* Feature engineering utilities
* AI model wrappers
* Production inference services

Encapsulation helps developers interact with these systems without needing to understand every implementation detail.

---

# 🧠 Key Takeaways

* Encapsulation protects object data.
* Public members are accessible everywhere.
* Protected members are intended for internal and subclass use.
* Private members use Name Mangling.
* Getters safely read private data.
* Setters validate data before updating it.
* `@property` creates cleaner, more Pythonic APIs.
* Encapsulation improves security, maintainability, and code quality.

---

# 📈 Skills Gained

After completing Day 19, I can:

* Design encapsulated classes.
* Protect sensitive object data.
* Implement validation using setters.
* Access private data using getters.
* Use `@property` effectively.
* Build secure and maintainable Python applications.
* Apply enterprise-level OOP principles.

---

# 🎯 OOP Milestone Achieved

After completing Day 19, I have successfully learned the **Four Pillars of Object-Oriented Programming**:

* ✅ Inheritance
* ✅ Polymorphism
* ✅ Abstraction
* ✅ Encapsulation

---

# 🎯 Next Step

In **Day 20**, I will learn:

* Composition
* Aggregation
* Association
* HAS-A Relationship
* IS-A vs HAS-A
* Enterprise OOP Design

I will continue extending the **Smart Vehicle Management System** and solve company-style coding challenges based on real software design scenarios.

---

# 📌 Day 19 Status

**Completed Successfully ✅**

# 🚀 Day 20 – Exception Handling in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-20-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Exception_Handling-orange?style=for-the-badge)

### 🛡️ Writing Robust Python Programs with Exception Handling

</div>

---

# 🎯 Goal of Day 20

Today I learned how to handle runtime errors in Python using **Exception Handling**.

The objective was to prevent programs from crashing unexpectedly and make them more reliable by handling errors gracefully.

By the end of today, I can:

* ✅ Understand runtime exceptions
* ✅ Use `try` and `except`
* ✅ Handle specific exceptions
* ✅ Use `else`
* ✅ Use `finally`
* ✅ Raise exceptions using `raise`
* ✅ Create custom exceptions
* ✅ Write cleaner and more reliable Python programs

---

# 📚 Topics Covered

## 🔹 What is an Exception?

An **exception** is an error that occurs while a program is running.

If an exception is not handled, Python stops executing the program.

---

## 🔹 Why Do We Need Exception Handling?

Without exception handling:

* Program crashes unexpectedly.
* Users receive confusing error messages.
* Data processing may stop.

With exception handling:

* Programs continue running whenever possible.
* Users receive meaningful error messages.
* Applications become more reliable.

---

# 🌍 Real-World Examples

## 📂 File Handling

If a required file does not exist, the program should display a meaningful message instead of crashing.

Example:

```text
File not found. Please check the file path.
```

---

## 👤 User Input Validation

If a user enters text instead of a number, the application should ask for valid input instead of terminating.

---

## 📊 Data Science Example

When loading datasets:

```python
import pandas as pd

try:
    df = pd.read_csv("sales.csv")
except FileNotFoundError:
    print("Dataset not found.")
```

This pattern is commonly used in data analysis and machine learning projects.

---

# 🔹 try and except

The `try` block contains code that may produce an exception.

The `except` block handles the exception if it occurs.

Example:

```python
try:
    num = int(input())
    print(100 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 🔹 Handling Specific Exceptions

I learned to handle common Python exceptions such as:

* ✅ `ValueError`
* ✅ `ZeroDivisionError`
* ✅ `FileNotFoundError`

Using specific exceptions makes code easier to understand and debug.

---

# 🔹 else

The `else` block executes **only when no exception occurs**.

Example:

```python
try:
    number = int(input())
except ValueError:
    print("Invalid input")
else:
    print("Valid input")
```

---

# 🔹 finally

The `finally` block executes **every time**, regardless of whether an exception occurs.

Example:

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Program finished")
```

It is commonly used for cleanup operations such as closing files or database connections.

---

# 🔹 raise

The `raise` keyword is used to generate exceptions manually.

Example:

```python
age = int(input())

if age < 18:
    raise ValueError("Age must be at least 18.")
```

This helps enforce business rules and validate user input.

---

# 🔹 Custom Exceptions

Python allows developers to create their own exception classes.

Example:

```python
class InvalidMarksError(Exception):
    pass
```

Custom exceptions make applications more organized and easier to maintain.

---

# 💻 Coding Practice Completed

Implemented programs for:

* ✅ Safe Division Calculator
* ✅ Age Validation
* ✅ File Reader with Exception Handling
* ✅ `try` – `except` – `else`
* ✅ `try` – `finally`
* ✅ Using `raise`
* ✅ Creating Custom Exceptions
* ✅ Marks Validation System

---

# 🌍 Practical Applications

Exception handling is used in:

* 📂 File Processing
* 🌐 API Requests
* 🗄️ Database Operations
* 📊 Data Analysis Projects
* 🤖 Machine Learning Pipelines
* ☁️ Enterprise Applications

---

# 🤖 Data Science Connection

Exception handling is an essential skill for Data Scientists because real-world data is often incomplete or inconsistent.

Typical use cases include:

* Reading CSV and Excel files
* Handling missing datasets
* Validating user input
* Managing API failures
* Preventing pipeline failures during data processing

---

# 🧠 Key Takeaways

* Exceptions are runtime errors.
* `try` contains risky code.
* `except` handles exceptions.
* `else` runs only if no exception occurs.
* `finally` always executes.
* `raise` creates exceptions manually.
* Custom exceptions improve code organization.
* Catch specific exceptions whenever possible instead of using a generic `except`.

---

# 📈 Skills Gained

After completing Day 20, I can:

* Handle runtime errors confidently.
* Prevent programs from crashing unexpectedly.
* Validate user input effectively.
* Use `else` and `finally` appropriately.
* Raise built-in exceptions.
* Create custom exceptions.
* Write more reliable and maintainable Python applications.

---

# 📊 Day 20 Performance

* 💻 Coding Practice: **40/40**
* 🧠 MCQs: **4/5**
* 🏆 Overall Score: **44/45 (97.8%)**

---

# 🎯 Next Step

In **Day 21**, I will learn:

* File Handling
* Reading Files
* Writing Files
* Appending Data
* File Modes (`r`, `w`, `a`, `x`)
* Working with `with open()`

These concepts are fundamental for handling datasets in Python before moving into NumPy, pandas, and other Data Science libraries.

---

# 📌 Day 20 Status

**Completed Successfully ✅**
# 🚀 Day 21 – File Handling in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-21-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-File_Handling-orange?style=for-the-badge)

### 📂 Reading, Writing & Managing Files in Python

</div>

---

# 🎯 Goal of Day 21

Today I learned how Python interacts with files stored on a computer.

I explored how to:

* Read data from files
* Write data to files
* Append new content
* Work with file pointers
* Handle file-related exceptions
* Use the industry-standard `with open()` approach

File handling is a fundamental skill because almost every Data Science and Machine Learning project starts by loading data from files such as CSV, JSON, Excel, or text files.

---

# 📚 Topics Covered

## 🔹 What is File Handling?

File handling is the process of creating, reading, writing, updating, and managing files using Python.

Unlike variables, files store data permanently even after the program finishes execution.

---

## 🔹 Opening Files

Used the `open()` function to access files.

Syntax:

```python
open("filename", "mode")
```

---

## 🔹 File Modes

| Mode | Purpose                       |
| ---- | ----------------------------- |
| `r`  | Read existing file            |
| `w`  | Write (creates or overwrites) |
| `a`  | Append data                   |
| `x`  | Create a new file             |
| `rb` | Read binary files             |
| `wb` | Write binary files            |

---

## 🔹 Reading Files

Learned to use:

```python
file.read()
```

Reads the entire file.

---

## 🔹 Writing Files

Learned:

```python
file.write()
```

Creates or overwrites file contents.

---

## 🔹 Appending Files

Using append mode:

```python
"a"
```

Adds new data without deleting existing content.

---

## 🔹 Exception Handling with Files

Handled situations like:

* File not found
* Invalid file paths

using:

```python
try:
    ...
except FileNotFoundError:
    ...
```

---

## 🔹 `readline()`

Reads one line at a time.

Useful for processing large files efficiently.

---

## 🔹 `readlines()`

Reads all lines and returns them as a list.

Example:

```python
['Siva\n', 'Rahul\n', 'Priya']
```

---

## 🔹 File Pointer

Every opened file has a pointer that tracks the current reading position.

---

## 🔹 `tell()`

Returns the current position of the file pointer.

---

## 🔹 `seek()`

Moves the file pointer to a specified location.

Useful when reading a file multiple times.

---

## 🔹 `with open()`

Industry-standard way of handling files.

Advantages:

* Automatically closes files
* Cleaner code
* Safer during exceptions
* Easier to maintain

---

## 🔹 Reading CSV Files

Learned that CSV files are plain text files containing comma-separated values.

Example:

```python
with open("students.csv", "r") as file:
    print(file.read())
```

This provides the foundation for later using:

```python
import pandas as pd

df = pd.read_csv("students.csv")
```

---

# 🌍 Real-World Applications

File handling is used in:

* 📊 Data Science
* 🤖 Machine Learning
* 🏦 Banking Systems
* 🏥 Hospital Management
* 🛒 E-commerce Platforms
* 📈 Business Reporting
* 📂 Log File Processing

---

# 💻 Coding Practice Completed

Implemented programs for:

* ✅ Creating text files
* ✅ Writing data
* ✅ Appending data
* ✅ Reading complete files
* ✅ Reading one line
* ✅ Reading all lines
* ✅ Using `tell()`
* ✅ Using `seek()`
* ✅ Handling `FileNotFoundError`

---

# 🤖 Data Science Connection

File handling is one of the first skills required in Data Science because datasets are commonly stored in:

* CSV files
* Excel files
* JSON files
* Text files

Understanding basic file operations makes it easier to work with libraries such as pandas later in the learning journey.

---

# 🧠 Key Takeaways

* Files store data permanently.
* Choose the correct file mode (`r`, `w`, `a`, `x`) based on the task.
* `read()` reads the entire file.
* `readline()` reads one line.
* `readlines()` returns all lines as a list.
* `tell()` shows the current file pointer position.
* `seek()` moves the file pointer.
* `with open()` is the recommended way to work with files.
* Handle file-related exceptions gracefully.

---

# 📈 Skills Gained

After completing Day 21, I can:

* Create and manage files in Python.
* Read and write text files.
* Append data safely.
* Use file pointers effectively.
* Handle common file-related exceptions.
* Read basic CSV files.
* Write cleaner and safer file-handling code using `with open()`.

---

# 📊 Day 21 Performance

* 💻 Coding Practice: **Completed ✅**
* 🧠 MCQs: **9/10**
* 📝 Theory Questions: **Completed ✅**
* 🏆 Overall Performance: **Excellent**

---

# 🎯 Next Step

In **Day 22**, I will learn:

* Python Modules
* Import Statements
* Built-in Modules
* Creating Custom Modules
* Packages
* `__name__ == "__main__"`
* Code Organization Best Practices

These concepts are essential for building scalable Python applications and preparing for Data Science, Machine Learning, and AI projects.

---

# 📌 Day 21 Status

**Completed Successfully ✅**

# 🚀 Day 22 – Modules & Packages in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-22-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Modules_&_Packages-orange?style=for-the-badge)

### 📦 Writing Modular, Reusable, and Organized Python Code

</div>

---

# 🎯 Goal of Day 22

Today I learned how to organize Python programs using **modules** and **packages**. I explored Python's built-in modules, created custom modules, and understood how professional Python projects are structured. I also learned about `pip`, virtual environments, and the importance of reusable code.

---

# 📚 Topics Covered

## 🔹 What is a Module?

A **module** is a Python (`.py`) file that contains reusable code such as functions, classes, and variables.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

Modules help avoid code duplication and make programs easier to maintain.

---

## 🔹 Importing Modules

Imported Python's built-in `math` module.

```python
import math

print(math.sqrt(49))
print(math.pi)
```

---

## 🔹 Importing Specific Functions

Imported only the required function.

```python
from math import factorial

print(factorial(6))
```

This makes the code cleaner when only a few functions are needed.

---

## 🔹 Aliases

Used aliases to simplify module names.

```python
import math as m

print(m.sqrt(100))
```

Common Data Science aliases:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## 🔹 Creating Custom Modules

Created a custom module and imported it into another Python file.

Example:

```python
# calculator.py

def add(a, b):
    return a + b

def divide(a, b):
    return a / b
```

```python
import calculator

print(calculator.add(10, 20))
```

---

## 🔹 What is a Package?

A **package** is a folder that contains related Python modules.

Example:

```text
utilities/
│── calculator.py
│── converter.py
│── validator.py
```

Packages help organize larger applications.

---

## 🔹 Module vs Package

| Module            | Package                            |
| ----------------- | ---------------------------------- |
| Single `.py` file | Folder containing multiple modules |
| Reusable code     | Collection of related modules      |

---

## 🔹 `__name__ == "__main__"`

Learned how Python identifies whether a file is being executed directly or imported as a module.

Example:

```python
if __name__ == "__main__":
    print("Program is running directly.")
```

This prevents test code from running when the module is imported into another program.

---

## 🔹 Python Standard Library

Explored commonly used built-in modules.

* `math`
* `random`
* `datetime`
* `os`
* `json`
* `csv`
* `sys`

These modules provide ready-to-use functionality without additional installation.

---

## 🔹 pip

Learned that **pip** is Python's package manager.

Example:

```bash
pip install pandas
pip install numpy
pip install matplotlib
```

It allows developers to install external libraries.

---

## 🔹 Virtual Environments

Learned why virtual environments are important.

Benefits:

* Isolate project dependencies
* Avoid version conflicts
* Improve project portability
* Support professional development workflows

---

## 🔹 Professional Project Structure

Example structure:

```text
project/

│── data/
│── notebooks/
│── src/
│── models/
│── README.md
│── requirements.txt
│── main.py
```

This organization improves readability, collaboration, and maintainability.

---

# 🌍 Real-World Applications

Modules and packages are used in:

* 📊 Data Science
* 🤖 Machine Learning
* 🌐 Web Development
* ☁️ Cloud Applications
* 📱 Software Development
* 🏦 Enterprise Systems

Almost every Python application is built using modules and packages.

---

# 💻 Coding Practice Completed

Implemented programs for:

* ✅ Importing built-in modules
* ✅ Using `math`
* ✅ Using aliases
* ✅ Importing specific functions
* ✅ Creating custom modules
* ✅ Using `random`
* ✅ Understanding `__name__ == "__main__"`

---

# 🤖 Data Science Connection

Every major Data Science library is built using modules and packages.

Examples:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
```

Understanding imports, packages, and project organization is essential before working with these libraries.

---

# 🧠 Key Takeaways

* Modules promote code reuse.
* Packages organize related modules.
* Use aliases such as `pd`, `np`, and `plt`.
* Avoid `from module import *` in professional projects.
* `__name__ == "__main__"` controls whether code runs directly or only when executed as the main program.
* `pip` installs third-party libraries.
* Virtual environments isolate project dependencies.
* Organized project structures improve collaboration and maintenance.

---

# 📈 Skills Gained

After completing Day 22, I can:

* Create and import Python modules.
* Build and use custom modules.
* Work with packages.
* Understand Python's Standard Library.
* Install libraries using `pip`.
* Explain the purpose of virtual environments.
* Organize Python projects using industry best practices.

---

# 📊 Day 22 Performance

* 💻 Coding Practice: **Completed ✅**
* 🧠 MCQs: **10/10**
* 📝 Theory: **Completed ✅**
* 🏆 Overall Performance: **Very Good**

---

# 🎯 Next Step

In **Day 23**, I will learn:

* Iterators
* Iterable Objects
* Iterator Protocol
* `iter()`
* `next()`
* Generators
* `yield`
* Generator Expressions

These concepts are widely used in Data Science for memory-efficient processing of large datasets and streaming data.

---

# 📌 Day 22 Status

**Completed Successfully ✅**


# 🚀 Day 23 – Iterators & Generators in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-23-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Iterators_&_Generators-orange?style=for-the-badge)

### ⚡ Memory-Efficient Data Processing with Python

</div>

---

# 🎯 Goal of Day 23

Today I learned how Python processes data efficiently using **iterators** and **generators**. I explored how to retrieve values one at a time, use the `yield` keyword, create generator expressions, and understand why these concepts are essential for handling large datasets in Data Science.

---

# 📚 Topics Covered

## 🔹 What is an Iterable?

An **iterable** is any object that can be traversed one element at a time.

Common examples include:

* Lists
* Tuples
* Strings
* Dictionaries
* Sets
* Ranges

Example:

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

---

## 🔹 What is an Iterator?

An **iterator** is an object that returns one element at a time.

Created using:

```python
iterator = iter(iterable)
```

Access elements using:

```python
next(iterator)
```

---

## 🔹 `iter()` Function

The `iter()` function converts an iterable into an iterator.

Example:

```python
numbers = [1, 2, 3]

it = iter(numbers)
```

---

## 🔹 `next()` Function

The `next()` function retrieves the next value from an iterator.

Example:

```python
print(next(it))
```

Each call moves the iterator forward.

---

## 🔹 StopIteration Exception

When no elements remain, Python raises:

```text
StopIteration
```

Handled using:

```python
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Iteration completed.")
```

---

## 🔹 What is a Generator?

A **generator** is a special function that uses the `yield` keyword to produce values one at a time.

Example:

```python
def numbers():
    yield 10
    yield 20
    yield 30
```

Generators pause after each `yield` and resume execution when requested.

---

## 🔹 `yield` Keyword

Unlike `return`, `yield` produces values lazily without terminating the function.

Example:

```python
gen = numbers()

print(next(gen))
```

---

## 🔹 Generator Expressions

A generator expression creates a generator using parentheses.

Example:

```python
squares = (x * x for x in range(1, 6))
```

Unlike list comprehensions, values are generated only when needed.

---

## 🔹 List Comprehension vs Generator Expression

| List Comprehension             | Generator Expression      |
| ------------------------------ | ------------------------- |
| Uses `[]`                      | Uses `()`                 |
| Creates all values immediately | Produces values on demand |
| Uses more memory               | Uses less memory          |

---

# 🌍 Real-World Applications

Iterators and generators are widely used in:

* 📊 Data Science
* 🤖 Machine Learning
* 📂 Large CSV file processing
* 📈 ETL pipelines
* 🌐 Streaming data
* 📝 Log analysis
* ☁️ Big Data applications

---

# 💻 Coding Practice Completed

Implemented programs for:

* ✅ Creating iterators
* ✅ Using `iter()`
* ✅ Using `next()`
* ✅ Handling `StopIteration`
* ✅ Creating generator functions
* ✅ Using `yield`
* ✅ Creating generator expressions

---

# 🤖 Data Science Connection

Large datasets often cannot fit entirely into memory.

Generators allow applications to:

* Process one record at a time
* Reduce memory consumption
* Improve scalability
* Build efficient data pipelines

This makes generators especially valuable in Data Science and Machine Learning workflows.

---

# 🧠 Key Takeaways

* An iterable can be looped over.
* An iterator returns one element at a time.
* `iter()` creates an iterator.
* `next()` retrieves the next element.
* `StopIteration` indicates the iterator has been exhausted.
* Generators use the `yield` keyword.
* Generator expressions are more memory efficient than list comprehensions.
* Lazy evaluation makes generators ideal for large datasets.

---

# 📈 Skills Gained

After completing Day 23, I can:

* Identify iterable objects.
* Create and use iterators.
* Handle `StopIteration` safely.
* Build generator functions.
* Use the `yield` keyword effectively.
* Create generator expressions.
* Explain the differences between iterators and generators.
* Apply memory-efficient techniques to Python programs.

---

# 📊 Day 23 Performance

* 💻 Coding Practice: **Completed ✅**
* 🧠 MCQs: **10/10**
* 📝 Theory: **Completed ✅**
* 🏆 Overall Performance: **Excellent**

---

# 🎯 Next Step

In **Day 24**, I will learn:

* Python Decorators
* Wrapper Functions
* `*args` and `**kwargs`
* Function Metadata
* Built-in Decorators
* Practical Decorator Examples

Decorators are widely used in frameworks such as Flask, Django, and FastAPI, making them an important topic for professional Python development.

---

# 📌 Day 23 Status

**Completed Successfully ✅**

# 🚀 Day 24 – Python Decorators

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-24-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Decorators-orange?style=for-the-badge)

### ⚡ Adding Functionality Without Modifying Existing Code

</div>

---

# 🎯 Goal of Day 24

Today I learned one of Python's most powerful features: **Decorators**. Decorators allow us to add extra functionality to a function without changing its original implementation.

---

# 📚 Topics Covered

## 🔹 What is a Decorator?

A decorator is a function that takes another function as input and returns a new function with additional behavior.

It helps us avoid repeating the same code across multiple functions.

---

## 🔹 Why Use Decorators?

Instead of writing the same logic repeatedly inside many functions, decorators let us write that logic once and reuse it.

Common use cases include:

* Logging
* Authentication
* Authorization
* Timing function execution
* Validation
* Caching

---

## 🔹 Basic Decorator

Example:

```python
def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper


@decorator
def greet():
    print("Hello")

greet()
```

Output:

```text
Before
Hello
After
```

---

## 🔹 Understanding the Wrapper Function

The **wrapper()** function contains the extra functionality that runs before and/or after the original function.

Flow:

```text
Call Function
      │
      ▼
Wrapper
      │
      ├── Before
      ├── Original Function
      └── After
```

---

## 🔹 `@decorator` Syntax

These two are equivalent:

```python
@decorator
def greet():
    print("Hello")
```

and

```python
def greet():
    print("Hello")

greet = decorator(greet)
```

The `@` symbol is simply cleaner syntax.

---

## 🔹 Decorators with `*args`

When the original function accepts positional arguments, the wrapper should also accept them.

Example:

```python
def decorator(func):

    def wrapper(*args):

        print("Before")

        func(*args)

        print("After")

    return wrapper
```

`*args` stores positional arguments as a **tuple**.

---

## 🔹 Decorators with `**kwargs`

For keyword arguments:

```python
def decorator(func):

    def wrapper(**kwargs):

        print("Before")

        func(**kwargs)

        print("After")

    return wrapper
```

`**kwargs` stores keyword arguments as a **dictionary**.

---

## 🔹 Universal Decorator

Most real-world decorators use both:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

This allows the decorator to work with almost any function.

---

## 🔹 `functools.wraps`

`functools.wraps` preserves the original function's metadata, such as:

* Function name
* Docstring
* Module information

Example:

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

---

# 🌍 Real-World Applications

Decorators are widely used in:

* Flask
* FastAPI
* Django
* Machine Learning pipelines
* Performance monitoring
* Logging systems
* Security and authentication
* API development

---

# 💻 Coding Practice

Practiced:

* ✅ Creating a basic decorator
* ✅ Understanding wrapper functions
* ✅ Using `@decorator`
* ✅ Passing positional arguments with `*args`
* ✅ Passing keyword arguments with `**kwargs`
* ✅ Preserving function metadata using `functools.wraps`

---

# 🧠 Key Takeaways

* A decorator adds functionality without modifying the original function.
* The wrapper function controls the execution flow.
* `@decorator` is shorthand for `function = decorator(function)`.
* `*args` accepts any number of positional arguments.
* `**kwargs` accepts any number of keyword arguments.
* `functools.wraps` preserves the original function's information.

---

# 📈 Skills Gained

After completing Day 24, I can:

* Create custom decorators.
* Explain how wrapper functions work.
* Decorate functions with and without arguments.
* Use `*args` and `**kwargs` in decorators.
* Understand the purpose of `functools.wraps`.
* Read and understand decorator-based Python code.

---

# 🎯 Next Step

**Day 25 – Context Managers**

Topics include:

* Context Managers
* `with` Statement
* `__enter__()` and `__exit__()`
* Creating Custom Context Managers
* File Handling Best Practices
* Practical Applications

---

# 📌 Day 24 Status

**Completed Successfully ✅**

# 👨‍💻 Author

**Siva Kumar Reddy**
# 🐍 Day 25 — Regular Expressions (Regex)

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-26-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Regular%20Expressions-orange?style=for-the-badge)

### 🔥 Mastering Pattern Matching & Text Processing with Python Regex

</div>

---

# 🎯 Goal of Day 25

Today I learned how to use **Regular Expressions (Regex)** in Python to search, extract, validate, replace, and manipulate text efficiently.

By the end of today, I can:

✅ Search Text Using Patterns
✅ Extract Useful Information
✅ Replace Matching Text
✅ Split Strings Using Patterns
✅ Validate User Input
✅ Clean Text for AI & Machine Learning

---

# 📚 What I Learned Today

## 🔹 Introduction to Regex

Regular Expressions (Regex) are patterns used to search, match, and manipulate text.

```python
import re
```

Regex is widely used in:

* Data Cleaning
* NLP
* Web Scraping
* Log Analysis
* Input Validation

---

## 🔹 `re.search()`

Searches the entire string for the first match.

```python
import re

text = "I am learning Python."

if re.search("Python", text):
    print("Found")
```

Output:

```text
Found
```

---

## 🔹 `re.match()`

Checks whether the pattern matches only at the beginning of the string.

```python
import re

text = "Python Programming"

print(re.match("Python", text))
```

---

## 🔹 `re.findall()`

Returns all matching values.

```python
import re

text = "Apple 25 Mango 100 Orange 350"

print(re.findall(r"\d+", text))
```

Output:

```python
['25', '100', '350']
```

---

## 🔹 `re.finditer()`

Returns an iterator of match objects.

```python
import re

text = "AI ML AI"

for match in re.finditer("AI", text):
    print(match.start())
```

---

## 🔹 `re.sub()`

Replaces matching text.

```python
import re

text = "Python is fun"

print(re.sub("fun", "awesome", text))
```

Output:

```text
Python is awesome
```

---

## 🔹 `re.split()`

Splits text using a regex pattern.

```python
import re

text = "Python,AI;ML Data"

print(re.split(r"[,; ]+", text))
```

Output:

```python
['Python', 'AI', 'ML', 'Data']
```

---

## 🔹 `re.compile()`

Compiles a regex pattern for repeated use.

```python
import re

pattern = re.compile(r"\d+")

print(pattern.findall("A12 B45 C78"))
```

---

# 🔍 Common Regex Patterns

| Pattern | Description           |
| ------- | --------------------- |
| `\d`    | Digit                 |
| `\D`    | Non-digit             |
| `\w`    | Word character        |
| `\W`    | Non-word character    |
| `\s`    | Whitespace            |
| `\S`    | Non-whitespace        |
| `.`     | Any character         |
| `^`     | Start of string       |
| `$`     | End of string         |
| `*`     | Zero or more          |
| `+`     | One or more           |
| `?`     | Zero or one           |
| `[]`    | Character set         |
| `[^]`   | Negated character set |

---

# 💻 Practice Programs Completed

* ✅ Search a Word in a String
* ✅ Extract Numbers
* ✅ Extract Email Address
* ✅ Replace Multiple Spaces
* ✅ Split Text Using Regex
* ✅ Count Digits
* ✅ Extract Customer IDs
* ✅ Extract Words Starting with a Specific Letter

---

# 🌍 Real-World AI/ML Connection

Regex is widely used in:

* 🤖 NLP Preprocessing
* 📊 Data Cleaning
* 📧 Email Validation
* 📱 Phone Number Validation
* 🔐 Password Validation
* 🌐 Web Scraping
* 📄 Resume Parsing
* 📜 Log File Analysis

Text preprocessing is one of the first steps in many AI and Machine Learning workflows.

---

# 🧠 Practice Programs Completed

* ✅ `re.search()`
* ✅ `re.match()`
* ✅ `re.findall()`
* ✅ `re.finditer()`
* ✅ `re.sub()`
* ✅ `re.split()`
* ✅ `re.compile()`
* ✅ Pattern Matching
* ✅ Email Extraction
* ✅ Data Cleaning
* ✅ Text Validation

---

# 📂 Project Structure

```text
day26/
│
├── search.py
├── match.py
├── findall.py
├── finditer.py
├── substitute.py
├── split.py
├── compile_pattern.py
├── email_extractor.py
├── number_extractor.py
├── data_cleaning.py
└── README.md
```

---

# ⚡ Why Regex Matters

Regular Expressions help developers:

* Search Text Efficiently
* Validate User Input
* Clean Datasets
* Extract Information
* Process Large Text Files
* Automate Text Analysis

Regex is an essential skill for Data Analysts, Data Scientists, and Machine Learning Engineers.

---

# 📈 Learning Progress

```text
Python Fundamentals   ████████████████ 100%
Object-Oriented Prog. ████████████████ 100%
Regex                 ████████████████ 100%

Problem Solving       ████████████████ 100%
AI/ML Journey         █████████████████░ 90%
```

---

# 💡 Day 26 Reflection

Today I learned how Regular Expressions simplify text processing using powerful pattern-matching techniques. I explored searching, extracting, replacing, and validating text, which are essential tasks in data preprocessing.

Regex is a valuable tool for preparing clean and structured data before analysis or machine learning model training.

> **"Clean data starts with powerful pattern matching, and Regex is one of the best tools for the job."**

---

# 🎯 Next Goals

* Date & Time Handling (`datetime`)
* NumPy
* Pandas
* Data Visualization
* Machine Learning Foundations

---
# 🐍 Day 27 — Lambda, Map, Filter & Reduce

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-27-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Functional%20Programming-orange?style=for-the-badge)

### 🔥 Writing Cleaner & More Efficient Python Code with Functional Programming

</div>

---

# 🎯 Goal of Day 27

Today I learned how to use **Lambda Functions**, **map()**, **filter()**, and **reduce()** to write concise and efficient Python programs.

By the end of today, I can:

✅ Create Lambda Functions
✅ Transform Data with `map()`
✅ Filter Data with `filter()`
✅ Aggregate Data with `reduce()`
✅ Chain Functional Programming Operations
✅ Process Data Efficiently

---

# 📚 What I Learned Today

## 🔹 Lambda Function

A **lambda function** is an anonymous function written in a single line.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```python
25
```

---

## 🔹 map()

Applies a function to every element in an iterable.

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Output:

```python
[2, 4, 6, 8]
```

---

## 🔹 filter()

Selects only the elements that satisfy a condition.

```python
numbers = [10, 20, 30, 40]

result = list(filter(lambda x: x > 20, numbers))

print(result)
```

Output:

```python
[30, 40]
```

---

## 🔹 reduce()

Combines all elements into a single value.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

Output:

```python
10
```

---

## 🔹 Chaining map(), filter() & reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
filtered = list(filter(lambda x: x > 5, doubled))
total = reduce(lambda x, y: x + y, filtered)

print(doubled)
print(filtered)
print(total)
```

Output:

```python
[2, 4, 6, 8, 10]
[6, 8, 10]
24
```

---

# 💻 Practice Programs Completed

* ✅ Lambda Function
* ✅ Square Calculator
* ✅ Double Numbers using `map()`
* ✅ Filter Even Numbers
* ✅ Filter Positive Numbers
* ✅ Sum using `reduce()`
* ✅ Product using `reduce()`
* ✅ Functional Programming Pipeline
* ✅ Salary Transformation
* ✅ Student Marks Filtering

---

# 🌍 Real-World AI/ML Connection

Functional programming is widely used in:

* 🤖 Machine Learning Data Pipelines
* 📊 Data Transformation
* 🧹 Data Cleaning
* ⚙️ ETL Processes
* 📈 Feature Engineering
* 💰 Financial Data Processing
* 🛒 E-commerce Analytics
* 📄 Log File Processing

These functions make data preprocessing faster, cleaner, and easier to maintain.

---

# 🧠 Key Concepts Learned

✅ Lambda Functions

✅ Anonymous Functions

✅ `map()`

✅ `filter()`

✅ `reduce()`

✅ Function Chaining

✅ Data Transformation

✅ Data Filtering

✅ Data Aggregation

✅ Functional Programming

---

# ⚠️ Common Mistakes

* Forgetting to convert `map()` and `filter()` objects into lists.
* Using `reduce()` without importing it from `functools`.
* Applying `filter()` before transforming the data when the opposite is intended.
* Trying to use `return` inside a lambda function.
* Overusing lambda expressions where a normal function would improve readability.

---

# 📂 Project Structure

```text
day27/
│
├── lambda_demo.py
├── map_examples.py
├── filter_examples.py
├── reduce_examples.py
├── chaining_operations.py
├── salary_processing.py
├── marks_filter.py
├── ecommerce_discount.py
├── data_pipeline.py
└── README.md
```

---

# ⚡ Why Functional Programming Matters

Functional programming helps developers:

* Write concise code
* Transform data efficiently
* Improve readability
* Process large datasets
* Build reusable data pipelines
* Simplify Machine Learning preprocessing

These concepts are widely used in Python libraries such as **Pandas**, **NumPy**, and **PySpark**.

---

# 📈 Learning Progress

```text
Python Fundamentals      ████████████████ 100%
Object-Oriented Prog.    ████████████████ 100%
Regular Expressions      ████████████████ 100%
Functional Programming   ████████████████ 100%

Problem Solving          ████████████████ 100%
AI/ML Journey            ██████████████████░ 92%
```

---

# 💡 Day 27 Reflection

Today I learned how functional programming simplifies data processing using **lambda functions**, **map()**, **filter()**, and **reduce()**. These tools make Python code more concise while improving efficiency when working with collections of data.

Functional programming is an important skill for Data Science and Machine Learning because many preprocessing tasks involve transforming, filtering, and aggregating large datasets.

> **"Clean data pipelines begin with clean, functional code."**

---

# 🎯 Next Goals

* List Comprehensions
* Dictionary Comprehensions
* Set Comprehensions
* NumPy
* Pandas
* Data Analysis Projects


# 👨‍💻 Author

**Siva**

📊 Aspiring AI/Data Scientist  
🚀 Building projects daily

---







