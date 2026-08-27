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

# 🌍 Practical Applications

Exception handling is used in:

* 📂 File Processing
* 🌐 API Requests
* 🗄️ Database Operations
* 📊 Data Analysis Projects
* 🤖 Machine Learning Pipelines
* ☁️ Enterprise Applications

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

# 🐍 Day 28 — List, Dictionary & Set Comprehensions

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-28-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Comprehensions-orange?style=for-the-badge)

### 🔥 Writing Cleaner, Faster & More Pythonic Code with Comprehensions

</div>

---

# 🎯 Goal of Day 28

Today I learned how to use **List**, **Dictionary**, and **Set Comprehensions** to create and transform collections efficiently.

By the end of today, I can:

✅ Create Lists Using Comprehensions
✅ Create Dictionaries Efficiently
✅ Build Sets with Unique Values
✅ Apply Conditional Filtering
✅ Transform Data in a Single Line
✅ Write More Pythonic Code

---

# 📚 What I Learned Today

## 🔹 List Comprehension

A list comprehension creates lists in a concise and readable way.

### Traditional Approach

```python
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)
```

### List Comprehension

```python
numbers = [i for i in range(1, 6)]

print(numbers)
```

Output:

```python
[1, 2, 3, 4, 5]
```

---

## 🔹 Creating Squares

```python
squares = [x ** 2 for x in range(1, 6)]

print(squares)
```

Output:

```python
[1, 4, 9, 16, 25]
```

---

## 🔹 List Comprehension with Condition

```python
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print(even_numbers)
```

Output:

```python
[2, 4, 6, 8, 10]
```

---

## 🔹 Dictionary Comprehension

Create dictionaries in a single line.

```python
square_dict = {x: x ** 2 for x in range(1, 6)}

print(square_dict)
```

Output:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

---

## 🔹 Dictionary Comprehension with Condition

```python
even_square_dict = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_square_dict)
```

Output:

```python
{
    2: 4,
    4: 16,
    6: 36,
    8: 64,
    10: 100
}
```

---

## 🔹 Set Comprehension

Create sets while automatically removing duplicate values.

```python
square_set = {x ** 2 for x in range(1, 6)}

print(square_set)
```

Output:

```python
{1, 4, 9, 16, 25}
```

---

## 🔹 Set Comprehension with Condition

```python
divisible_by_three = {
    x
    for x in range(1, 16)
    if x % 3 == 0
}

print(divisible_by_three)
```

Output:

```python
{3, 6, 9, 12, 15}
```

# 🌍 Real-World AI/ML Connection

Comprehensions are widely used in:

* 🤖 Data Preprocessing
* 📊 Data Transformation
* 🧹 Data Cleaning
* ⚙️ ETL Pipelines
* 📈 Feature Engineering
* 🌐 API Response Processing
* 🛒 Business Analytics
* 🧠 Machine Learning Workflows

They help process large datasets with clean and efficient code.

# 💼 Industry Examples

## Remove Empty Strings

```python
names = ["Siva", "", "Kumar", "", "Reddy"]

clean_names = [name for name in names if name != ""]

print(clean_names)
```

---

## Apply Salary Hike

```python
salaries = [25000, 40000, 55000]

updated_salaries = [salary * 1.15 for salary in salaries]

print(updated_salaries)
```

---

## Filter Passed Students

```python
marks = {
    "Rahul": 85,
    "Anita": 45,
    "Siva": 92
}

passed_students = {
    name: score
    for name, score in marks.items()
    if score >= 50
}

print(passed_students)
```
# 🐍 Day 29 — `zip()`, `enumerate()`, `any()` & `all()`

<div align="center">

![Python](https://img.shields.io/badge/Python-Intermediate-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-29-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Built--in%20Functions-orange?style=for-the-badge)

### 🔥 Writing Smarter & More Pythonic Code with Powerful Built-in Functions

</div>

---

# 🎯 Goal of Day 29

Today I learned four powerful built-in Python functions: **`zip()`**, **`enumerate()`**, **`any()`**, and **`all()`**.

By the end of today, I can:

✅ Combine Multiple Iterables with `zip()`
✅ Iterate with Index Using `enumerate()`
✅ Validate Data Using `any()`
✅ Verify Conditions Using `all()`
✅ Write Cleaner & More Efficient Python Code

---

# 📚 What I Learned Today

## 🔹 `zip()`

`zip()` combines two or more iterables element by element.

```python
names = ["Siva", "Rahul", "Priya"]
marks = [85, 90, 78]

result = list(zip(names, marks))

print(result)
```

Output:

```python
[('Siva', 85), ('Rahul', 90), ('Priya', 78)]
```

---

## 🔹 Creating a Dictionary with `zip()`

```python
keys = ["name", "age", "city"]
values = ["Siva", 22, "Vijayawada"]

student = dict(zip(keys, values))

print(student)
```

Output:

```python
{
    "name": "Siva",
    "age": 22,
    "city": "Vijayawada"
}
```

---

## 🔹 `enumerate()`

Returns both the index and value while iterating.

```python
fruits = ["Apple", "Mango", "Orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 Apple
1 Mango
2 Orange
```

---

## 🔹 Custom Starting Index

```python
students = ["Rahul", "Siva", "Priya"]

for roll_no, student in enumerate(students, start=101):
    print(roll_no, student)
```

Output:

```text
101 Rahul
102 Siva
103 Priya
```

---

## 🔹 `any()`

Returns **True** if at least one value is truthy.

```python
numbers = [0, 0, 5, 0]

print(any(numbers))
```

Output:

```python
True
```

---

## 🔹 `any()` with Generator Expression

```python
attendance = [True, True, False, True]

print(any(not status for status in attendance))
```

Output:

```python
True
```

This checks whether **any employee is absent**.

---

## 🔹 `all()`

Returns **True** only if every value is truthy.

```python
numbers = [2, 4, 6, 8]

print(all(i % 2 == 0 for i in numbers))
```

Output:

```python
True
```

---

## 🔹 Student Validation

```python
marks = [75, 82, 91, 68]

print(all(mark >= 35 for mark in marks))
```

Output:

```python
True
```

# 🌍 Real-World AI/ML Connection

These built-in functions are widely used in:

* 🤖 Machine Learning Data Processing
* 📊 Data Analysis
* 🧹 Data Validation
* 📈 Feature Engineering
* ⚙️ ETL Pipelines
* 📄 CSV Processing
* 🌐 API Data Handling
* 📋 Business Rule Validation

They simplify data manipulation while improving code readability and efficiency.

# 💼 Industry Examples

## Pair Employee Names with Salaries

```python
employees = ["Rahul", "Siva", "Priya"]
salaries = [50000, 65000, 55000]

employee_salary = dict(zip(employees, salaries))

print(employee_salary)
```

---

## Validate User Passwords

```python
passwords = ["Python123", "AI@2026", "ML2025"]

print(all(len(password) >= 8 for password in passwords))
```

---

## Detect Missing Records

```python
records = [100, 200, None, 400]

print(any(record is None for record in records))
```



# 🐍 Day 30 — `*args`, `**kwargs`, Variable Scope & JSON

<div align="center">

![Python](https://img.shields.io/badge/Python-Advanced-blue?style=for-the-badge\&logo=python)
![Day](https://img.shields.io/badge/Day-30-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Advanced%20Python-orange?style=for-the-badge)

### 🎉 Completing the Python Foundation for Data Science & Machine Learning

</div>

---

# 🎯 Goal of Day 30

Today I completed the final day of my Python roadmap by learning advanced Python concepts used in real-world software development, Data Science, Machine Learning, and APIs.

By the end of today, I can:

✅ Use `*args` for Variable Positional Arguments
✅ Use `**kwargs` for Variable Keyword Arguments
✅ Understand Variable Scope (`local`, `global`, `nonlocal`)
✅ Work with JSON Data
✅ Build Flexible & Production-Ready Python Functions

---

# 📚 What I Learned Today

## 🔹 `*args`

`*args` allows a function to accept any number of positional arguments.

```python id="lqjmsw"
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30, 40))
```

Output:

```text id="a6tbw2"
100
```

---

## 🔹 `**kwargs`

`**kwargs` allows a function to accept any number of keyword arguments.

```python id="mwczfv"
def student(**details):
    print(details["name"])
    print(details["age"])

student(name="Siva", age=22)
```

Output:

```text id="6bzr3g"
Siva
22
```

---

## 🔹 Local Variable

A local variable exists only inside the function.

```python id="nm2g3h"
def demo():
    x = 10
    print(x)

demo()
```

---

## 🔹 Global Variable

A global variable can be accessed throughout the program.

```python id="xiuqfw"
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
```

Output:

```text id="ev2foq"
1
```

---

## 🔹 `nonlocal`

Used inside nested functions to modify variables from the enclosing function.

```python id="wjlwm0"
def outer():
    x = 100

    def inner():
        nonlocal x
        x += 50

    inner()
    print(x)

outer()
```

Output:

```text id="3qff4p"
150
```

---

## 🔹 JSON

JSON (JavaScript Object Notation) is the standard format for exchanging structured data.

```python id="5jv0i5"
import json
```

---

## 🔹 Python Dictionary → JSON

```python id="6hbp7x"
import json

student = {
    "name": "Siva",
    "age": 22
}

json_data = json.dumps(student)

print(json_data)
```

Output:

```text id="r65x2j"
{"name": "Siva", "age": 22}
```

---

## 🔹 JSON → Python Dictionary

```python id="f24g1d"
import json

data = '{"name":"Siva","age":22}'

student = json.loads(data)

print(student)
```

Output:

```python id="bz1rxf"
{'name': 'Siva', 'age': 22}
```

---

## 🔹 Pretty Printing JSON

```python id="2bbo3g"
import json

employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 65000
}

print(json.dumps(employee, indent=4))
```

---

# 💻 Practice Programs Completed

* ✅ `*args` Examples
* ✅ `**kwargs` Examples
* ✅ Local Variables
* ✅ Global Variables
* ✅ `nonlocal` Variables
* ✅ JSON Serialization
* ✅ JSON Deserialization
* ✅ Pretty JSON Printing
* ✅ Flexible Calculator
* ✅ Student Information System

---

# 🌍 Real-World AI/ML Connection

These concepts are widely used in:

* 🤖 Machine Learning APIs
* 🌐 REST API Development
* 📊 Data Science Pipelines
* ⚙️ Automation Scripts
* ☁️ Cloud Applications
* 📁 Configuration Management
* 🔄 Data Exchange Between Systems
* 🧠 AI & LLM Applications

JSON is the most common format for transferring data between applications and services.

---

# 🧠 Key Concepts Learned

✅ `*args`

✅ `**kwargs`

✅ Local Variables

✅ Global Variables

✅ `nonlocal`

✅ JSON

✅ `json.dumps()`

✅ `json.loads()`

✅ Flexible Functions

✅ Data Serialization

---

# 💼 Industry Examples

## Flexible Calculator

```python id="wh0mrl"
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30, 40, 50))
```

---

## Employee Configuration

```python id="kryvze"
def employee(**details):
    print(details)

employee(name="Rahul", department="AI", salary=60000)
```

---

## API Response

```python id="nhd7jx"
import json

response = {
    "status": "Success",
    "prediction": "Approved"
}

print(json.dumps(response, indent=4))
```

# 📊 Day 31 — Introduction to Statistics for Data Science & Generative AI

<div align="center">

![Statistics](https://img.shields.io/badge/Statistics-Foundation-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-31-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Introduction%20to%20Statistics-orange?style=for-the-badge)

### 🚀 Beginning the Mathematics Journey for Data Science & Generative AI

</div>

# 📚 What I Learned Today

## 🔹 What is Statistics?

Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data to support decision-making.

It forms the mathematical foundation for:

* 📊 Data Science
* 🤖 Machine Learning
* 🧠 Artificial Intelligence
* ✨ Generative AI
* 📈 Business Analytics

---

## 🔹 Population vs Sample

### Population

The complete collection of observations under study.

**Examples**

* Every customer of an e-commerce platform
* Every student in a university

---

### Sample

A subset of the population selected for analysis.

**Examples**

* 10,000 customers selected from 5 million users
* 500 students selected from an entire university

---

## 🔹 Variables

A variable is a characteristic measured for each observation.

Examples:

* Age
* Salary
* Height
* Department
* Purchase Amount

---

## 🔹 Observations

Each row in a dataset represents one observation.

| Name  | Age | Salary |
| ----- | --: | -----: |
| Rahul |  24 |  35000 |

This row represents one observation.

---

## 🔹 Types of Data

### Qualitative (Categorical)

Examples:

* Gender
* City
* Blood Group
* Payment Method

---

### Quantitative (Numerical)

Examples:

* Salary
* Height
* Weight
* Temperature

#### Discrete Data

Countable values.

Examples:

* Number of Students
* Number of Orders

#### Continuous Data

Measured values.

Examples:

* Height
* Weight
* Temperature

---

# 💻 Python Practice

Performed basic statistical analysis using **Pure Python**.

### Count Observations

```python
marks = [72, 85, 91, 67, 88]

print(len(marks))
```

---

### Calculate Total

```python
marks = [72, 85, 91, 67, 88]

print(sum(marks))
```

---

### Calculate Mean

```python
marks = [72, 85, 91, 67, 88]

total = sum(marks)
count = len(marks)
mean = total / count

print(mean)
```

---

### Find Maximum

```python
marks = [72, 85, 91, 67, 88]

print(max(marks))
```

---

### Find Minimum

```python
marks = [72, 85, 91, 67, 88]

print(min(marks))
```

# 🌍 Real-World Data Science & AI Connection

Statistics is the backbone of modern data-driven systems.

It is used in:

* 📊 Business Intelligence
* 📈 Sales Analysis
* 🛒 Customer Analytics
* 💳 Fraud Detection
* 🧪 A/B Testing
* 🤖 Machine Learning
* 🧠 Generative AI
* 📉 Model Performance Evaluation

Understanding statistics is essential before building predictive models or AI applications.

# ⚡ Why Statistics Matters

Statistics helps professionals:

* Understand datasets
* Identify trends and patterns
* Support business decisions
* Build accurate Machine Learning models
* Evaluate AI system performance
* Make data-driven decisions

Every successful Data Scientist and ML Engineer relies on statistical thinking.


# 📊 Day 32 — Arithmetic Mean & Weighted Mean

<div align="center">

![Statistics](https://img.shields.io/badge/Statistics-Central%20Tendency-blue?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-32-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Arithmetic%20Mean%20%26%20Weighted%20Mean-orange?style=for-the-badge)

### 🚀 Understanding the Most Important Measure of Central Tendency

</div>

# 📚 What I Learned Today

## 🔹 Arithmetic Mean

Arithmetic Mean is the sum of all observations divided by the total number of observations.

### Formula

[
\text{Mean}=\frac{\sum x}{n}
]

Where:

* **Σx** → Sum of all observations
* **n** → Number of observations

### Example

```text
Marks = 70, 80, 90, 60, 100

Total = 400
Students = 5

Mean = 400 / 5 = 80
```

---

## 🔹 Weighted Mean

Weighted Mean is used when some observations are more important than others.

### Formula

[
\text{Weighted Mean}=\frac{\sum(wx)}{\sum w}
]

Where:

* **w** → Weight
* **x** → Observation

### Example

| Component  | Weight | Score |
| ---------- | -----: | ----: |
| Assignment |    20% |    85 |
| Mid Exam   |    30% |    75 |
| Final Exam |    50% |    90 |

Calculation:

```text
(85 × 0.2) + (75 × 0.3) + (90 × 0.5)

17 + 22.5 + 45

Weighted Mean = 84.5
```

---

# 🔄 Arithmetic Mean vs Weighted Mean

| Arithmetic Mean                 | Weighted Mean                       |
| ------------------------------- | ----------------------------------- |
| Equal importance to every value | Different importance for each value |
| Simple average                  | Weighted average                    |
| Easy to calculate               | Requires weights                    |
| Used for general summaries      | Used when priorities are assigned   |

---

# 💻 Pure Python Practice

### Arithmetic Mean

```python
marks = [70, 80, 90, 60, 100]

total = sum(marks)
count = len(marks)
mean = total / count

print("Total Marks:", total)
print("Students:", count)
print("Arithmetic Mean:", mean)
```

---

### Average Customer Spending

```python
spending = [500, 700, 900, 400, 1000]

total = sum(spending)
average = total / len(spending)

print("Average Spending:", average)
```

---

### Employee Salary Analysis

```python
salary = [30000, 45000, 50000, 35000]

print("Highest Salary:", max(salary))
print("Lowest Salary:", min(salary))
print("Average Salary:", sum(salary) / len(salary))
```

# 🌍 Real-World Data Science & AI Connection

Mean is one of the most commonly used statistical measures across industries.

### 📊 Data Science

* Customer spending analysis
* Sales performance
* Employee salary analysis
* Business reporting

### 🤖 Machine Learning

* Mean Squared Error (MSE)
* Average prediction accuracy
* Feature analysis
* Model evaluation

### ✨ Generative AI

* Average prompt length
* Average response time
* Token usage analysis
* Inference latency monitoring

# ⚠️ Common Mistakes

* Forgetting to divide by the total number of observations.
* Confusing Arithmetic Mean with Weighted Mean.
* Ignoring weights while calculating Weighted Mean.
* Using Mean for categorical data.
* Forgetting that outliers can significantly affect the Mean.


# 📊 Day 33 – Statistics for Data Science + Generative AI

## Median & Mode

# 📚 Topics Covered

## 1. Median

The Median is the middle value of a dataset after arranging the observations in ascending order.

### Odd Number of Observations

Example:

```text
40, 60, 70, 80, 90
```

Median:

```text
70
```

### Even Number of Observations

Example:

```text
50, 70, 80, 90
```

Median:

```text
(70 + 80) / 2 = 75
```

---

# 2. Mode

Mode is the value that occurs most frequently in a dataset.

Example:

```text
2, 3, 3, 4, 5
```

Mode:

```text
3
```

### Types of Mode

* **Unimodal** → One mode
* **Bimodal** → Two modes
* **Multimodal** → More than two modes
* **No Mode** → No value occurs more frequently than the others

Mode can also be applied to **categorical data**.

Example:

```text
UPI, Cash, UPI, Card, UPI
```

Mode = `UPI`

---

# 🔄 Mean vs Median vs Mode

| Measure | Main Use                                       |
| ------- | ---------------------------------------------- |
| Mean    | Average of numerical observations              |
| Median  | Typical middle value, especially with outliers |
| Mode    | Most frequently occurring value                |

---

# ⚠️ Outliers and Median

Consider employee salaries:

```text
25000
27000
28000
30000
800000
```

The extreme salary significantly increases the Mean.

The Median remains closer to the typical employee salary.

Therefore, Median is often more appropriate for **skewed datasets** or datasets containing extreme values.

---

# 💻 Implementation

## Pure Python – Median

```python
marks = [72, 85, 91, 67, 88]

sorted_list = sorted(marks)
middle_index = len(sorted_list) // 2
middle_element = sorted_list[middle_index]

print(sorted_list)
print(middle_element)
```

---

## NumPy – Median

```python
import numpy as np

marks = [72, 85, 91, 67, 88]

median = np.median(marks)

print(median)
```

### Important

NumPy provides:

```python
np.median()
```

but does **not** provide a basic:

```python
np.mode()
```

function.

---

## Pure Python – Mode

```python
ratings = [4, 5, 4, 3, 5, 4, 2]

frequency = {}

for rating in ratings:
    frequency[rating] = frequency.get(rating, 0) + 1

mode = max(frequency, key=frequency.get)

print(mode)
```

Output:

```text
4
```

---

## Pandas – Mode

```python
import pandas as pd

ratings = [4, 5, 4, 3, 5, 4, 2]

data = pd.Series(ratings)

print(data.mode())
```

---

# 📊 Mini Data Science Example

```python
import pandas as pd

data = pd.DataFrame({
    "Customer": ["A", "B", "C", "D", "E", "F", "G"],
    "Purchase": [500, 700, 500, 900, 1200, 500, 800]
})

print(data["Purchase"].mean())
print(data["Purchase"].median())
print(data["Purchase"].mode())
print(data["Purchase"].max())
print(data["Purchase"].min())
```

### Results

* Mean = **700**
* Median = **500**
* Mode = **500**
* Maximum = **1200**
* Minimum = **500**

---

# 🌍 Data Science Applications

### Median

* Employee salary analysis
* House prices
* Customer spending
* Response latency
* Income analysis

### Mode

* Most common payment method
* Most purchased product
* Most common customer category
* Most common prompt category

---

# 🤖 AI & Generative AI Applications

### Median

Can be useful for analyzing:

* Chatbot response latency
* Model inference time
* Token processing time

Especially when occasional extreme values distort the Mean.

### Mode

Can be used to identify:

* Most common prompt category
* Most frequent user intent
* Most common classification output

---

## Day 34 – Mean vs Median vs Mode + Outliers
# 📚 Topics Covered

## 1. Mean

Mean represents the arithmetic average of numerical observations.

### Formula

```text
Mean = Sum of all observations / Number of observations
```

### Example

```text
10, 20, 30, 40, 50

Mean = (10 + 20 + 30 + 40 + 50) / 5
     = 150 / 5
     = 30
```

### Python

```python
data = [10, 20, 30, 40, 50]

mean = sum(data) / len(data)

print("Mean:", mean)
```

### NumPy

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
```

### Pandas

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])

print("Mean:", data.mean())
```

---

## 2. Median

Median is the **middle value** when the data is arranged in ascending or descending order.

### Example — Odd Number of Observations

```text
10, 20, 30, 40, 50

Median = 30
```

### Example — Even Number of Observations

```text
10, 20, 30, 40

Median = (20 + 30) / 2
       = 25
```

### Python

```python
data = [10, 20, 30, 40, 50]

data.sort()

n = len(data)

if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2

print("Median:", median)
```

### NumPy

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Median:", np.median(data))
```

### Pandas

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])

print("Median:", data.median())
```

---

## 3. Mode

Mode is the value that occurs **most frequently** in a dataset.

### Example

```text
10, 20, 20, 30, 40

Mode = 20
```

### Python

```python
from collections import Counter

data = [10, 20, 20, 30, 40]

mode = Counter(data).most_common(1)[0][0]

print("Mode:", mode)
```

### Pandas

```python
import pandas as pd

data = pd.Series([10, 20, 20, 30, 40])

print("Mode:", data.mode().tolist())
```

---

# 4. Mean vs Median vs Mode

| Measure | Meaning             | Sensitive to Outliers? | Common Use                          |
| ------- | ------------------- | ---------------------- | ----------------------------------- |
| Mean    | Average value       | Yes                    | Normally distributed numerical data |
| Median  | Middle value        | No / much less         | Skewed data                         |
| Mode    | Most frequent value | Usually no             | Categorical or repeated values      |

### Example 1 — Normal Data

```text
10, 20, 30, 40, 50

Mean   = 30
Median = 30
```

Mean and Median are similar because there is no extreme value.

### Example 2 — Data with an Outlier

```text
10, 20, 30, 40, 500

Mean   = 120
Median = 30
```

The value `500` dramatically increases the Mean, while the Median remains `30`.

---

# 5. What is an Outlier?

An **outlier** is an observation that is unusually far away from the majority of the data.

### Example 1 — Salary

```text
25000
28000
30000
32000
35000
800000
```

`800000` is an obvious outlier compared with the other salaries.

### Example 2 — Website Response Time

```text
120 ms
130 ms
125 ms
140 ms
135 ms
5000 ms
```

`5000 ms` is an extreme observation and may indicate a system problem.

---

# 6. Effect of Outliers on Mean

Mean is highly sensitive to extreme values.

### Example

Without outlier:

```text
10, 20, 30, 40, 50

Mean = 30
```

With outlier:

```text
10, 20, 30, 40, 500

Mean = 120
```

The Median remains:

```text
30
```

### Key Insight

> **Outliers can pull the Mean toward extreme values.**

Therefore, using Mean blindly can produce a misleading representation of the typical observation.

---

# 7. Why Median is Robust to Outliers

Median depends on the **position of observations**, not their magnitude.

Consider:

```text
10, 20, 30, 40, 50
```

Median:

```text
30
```

Now replace `50` with `500000`:

```text
10, 20, 30, 40, 500000
```

Median is still:

```text
30
```

The extreme value has almost no effect on the Median.

---

# 8. Right-Skewed Data

Right-skewed data contains a long tail toward higher values.

Usually:

```text
Mean > Median
```

### Example

Income data:

```text
20K, 22K, 25K, 28K, 30K, 500K
```

A few very high salaries pull the Mean upward.

### Business Example

For employee salaries in a company, Median salary may provide a better representation of the **typical employee salary** when a small number of executives earn extremely high salaries.

---

# 9. Left-Skewed Data

Left-skewed data contains a long tail toward lower values.

Usually:

```text
Mean < Median
```

### Example

```text
10, 70, 80, 85, 90, 95
```

The low value pulls the Mean downward.

### Business Example

If most customers give high product ratings but a small number give extremely low ratings, the Mean can be pulled downward.

---

# 10. Relationship Between Mean and Median

A useful rule of thumb:

```text
Symmetric Distribution:
Mean ≈ Median

Right-Skewed Distribution:
Mean > Median

Left-Skewed Distribution:
Mean < Median
```

This relationship can help identify the general shape of a distribution.

> Note: These are rules of thumb, not universal laws. Real datasets can violate them.

---

# 11. Choosing the Right Measure

### Use Mean when:

* Data is approximately symmetric.
* There are no major outliers.
* Every numerical observation should contribute proportionally.

**Example:**

Average temperature over a week.

```text
28, 29, 30, 31, 30, 29, 28
```

Mean is reasonable.

---

### Use Median when:

* Data is skewed.
* Outliers are present.
* You want the typical observation.

**Example:**

House prices:

```text
₹40L, ₹45L, ₹50L, ₹55L, ₹5Cr
```

Median is generally more representative than Mean.

---

### Use Mode when:

* You want the most frequently occurring value.
* Data is categorical.
* Frequency is more meaningful than average.

**Example:**

Most common customer payment method:

```text
UPI, Card, UPI, Cash, UPI, Card
```

Mode:

```text
UPI
```

---

# 12. Pure Python Statistical Analysis

```python
from collections import Counter

data = [10, 20, 20, 30, 40, 50]

# Mean
mean = sum(data) / len(data)

# Median
sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 1:
    median = sorted_data[n // 2]
else:
    median = (
        sorted_data[n // 2 - 1] +
        sorted_data[n // 2]
    ) / 2

# Mode
mode = Counter(data).most_common(1)[0][0]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
```

---

# 13. NumPy Statistical Analysis

```python
import numpy as np

data = np.array([10, 20, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
```

NumPy is useful for fast numerical and statistical operations on arrays.

---

# 14. Pandas Statistical Analysis

```python
import pandas as pd

data = pd.Series([10, 20, 20, 30, 40, 50])

print("Mean:", data.mean())
print("Median:", data.median())
print("Mode:", data.mode().tolist())
```

Pandas is especially useful when working with real-world datasets stored in DataFrames.

---

# 15. Business Problem — Salary Analysis

Consider:

```python
import pandas as pd

data = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Salary": [25000, 28000, 30000, 32000, 35000, 800000]
})

print("Mean Salary:", data["Salary"].mean())
print("Median Salary:", data["Salary"].median())
print("Mode Salary:", data["Salary"].mode().tolist())
```

# 📊 Day 35 — Quartiles & Percentiles

<p align="center">
  <img src="https://img.shields.io/badge/Day-35-2563EB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Statistics-Quartiles%20%26%20Percentiles-7C3AED?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.x-F7DF1E?style=for-the-badge&logo=python&logoColor=black" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas" />
</p>

<p align="center">
  <b>Mathematics for Data Science + Generative AI</b>
</p>

---

## 📌 Overview

Day 35 focused on **quartiles and percentiles** — statistical techniques used to understand the relative position of observations within a dataset.

The core question was:

> **Where does a particular value stand compared with the rest of the data?**

The concepts were implemented with **Python, NumPy, and Pandas**, then connected to practical Data Science and AI/GenAI scenarios including customer analytics, API performance, and LLM latency monitoring.

---

## 🎯 Learning Outcomes

By completing this module, I can:

* Explain **Q1, Q2, and Q3**
* Interpret **P25, P50, P75, P90, P95, and P99**
* Relate quartiles to percentiles
* Calculate quartiles using the **median-of-halves method**
* Understand percentile position and interpolation
* Distinguish **percentage vs percentile**
* Calculate percentiles using **NumPy**
* Calculate quantiles using **Pandas**
* Use **IQR for potential outlier detection**
* Interpret percentiles in business scenarios
* Explain why **P95/P99** matter in AI/API latency monitoring

---

## 🧠 Core Concepts

### Quartiles

Quartiles divide ordered observations into approximately four sections.

```text
Q1        Q2        Q3
│         │         │
25%       50%       75%
```

| Measure | Equivalent   |
| ------- | ------------ |
| **Q1**  | P25          |
| **Q2**  | P50 = Median |
| **Q3**  | P75          |

### Percentiles

Percentiles describe the relative position of a value within a distribution.

```text
P25   → 25th percentile
P50   → 50th percentile
P75   → 75th percentile
P90   → 90th percentile
P95   → 95th percentile
P99   → 99th percentile
```

---

## 🧪 Practical Example

Dataset:

```text
10, 20, 30, 40, 50, 60, 70
```

Using the **median-of-halves method**:

```text
Q1 = 20
Q2 = 40
Q3 = 60
```

### Interquartile Range

```text
IQR = Q3 - Q1
    = 60 - 20
    = 40
```

---

<details>
<summary><b>🐍 NumPy Implementation</b></summary>

```python
import numpy as np

data = [10, 20, 30, 40, 50, 60, 70]

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
```

</details>

<details>
<summary><b>🐼 Pandas Implementation</b></summary>

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40, 50, 60, 70])

print("Q1:", data.quantile(0.25))
print("Q2:", data.quantile(0.50))
print("Q3:", data.quantile(0.75))
```

</details>

<details>
<summary><b>🚨 IQR & Outlier Detection</b></summary>

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Values outside these boundaries can be treated as **potential outliers** under the IQR rule.

</details>

---

## 💼 Real-World Applications

### Customer Analytics

Percentiles can help identify differences in customer spending and support segmentation.

```text
P25 → Lower-spending segment
P50 → Median customer
P75 → Higher-spending segment
```

# 📊 Day 36 — Range & Interquartile Range (IQR)

# 📚 1. Range

Range is the difference between the maximum and minimum values.

## Formula

```text
Range = Maximum - Minimum
```

### Example

```text
Data = 10, 20, 30, 40, 50

Range = 50 - 10
      = 40
```

### Limitation

Range depends only on the **minimum and maximum values**, so a single extreme value can significantly change it.

---

# 📚 2. Interquartile Range (IQR)

IQR measures the spread of the **middle 50% of the data**.

## Formula

```text
IQR = Q3 - Q1
```

Where:

* **Q1** = 25th percentile
* **Q3** = 75th percentile

### Example

```text
Q1 = 20
Q3 = 50

IQR = 50 - 20
    = 30
```

---

# 📊 3. Range vs IQR

| Measure | Measures          | Sensitive to Outliers? |
| ------- | ----------------- | ---------------------- |
| Range   | Overall spread    | Yes                    |
| IQR     | Middle 50% spread | Much less              |

### Key Insight

> **Range tells us how wide the entire dataset is, while IQR tells us how spread out the central 50% is.**

---

# 🚨 4. IQR and Outlier Detection

The **1.5 × IQR rule** is commonly used to identify potential outliers.

## Lower Boundary

```text
Lower Bound = Q1 - 1.5 × IQR
```

## Upper Boundary

```text
Upper Bound = Q3 + 1.5 × IQR
```

Values outside these boundaries are considered **potential outliers**.

### Example

```text
Q1 = 20
Q3 = 50

IQR = 50 - 20
    = 30
```

```text
Lower Bound = 20 - (1.5 × 30)
            = -25
```

```text
Upper Bound = 50 + (1.5 × 30)
            = 95
```

Therefore:

```text
Values < -25 → Potential outliers
Values > 95  → Potential outliers
```

---

# ⚠️ 5. Outlier ≠ Bad Data

An outlier is a value that is unusually far from the rest of the observations.

It does **not automatically mean the data is incorrect**.

### Example 1 — Business

A company has employee salaries between ₹25,000 and ₹60,000, but the CEO earns ₹2,50,000.

The CEO's salary may be a statistical outlier, but it is **valid data**.

### Example 2 — AI/GenAI

Most model response times are between 1–3 seconds, but one request takes 15 seconds.

That observation may be an outlier because of:

* Large input
* API latency
* Server load
* Network issues
* Model processing complexity

The correct approach is to **investigate the outlier**, not automatically delete it.

---

# 🐍 6. NumPy Implementation

```python
import numpy as np

data = [10, 20, 30, 40, 50, 60, 70]

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
```

---

# 🐼 7. Pandas Implementation

```python
import pandas as pd

data = pd.DataFrame({
    "Salary": [25000, 28000, 30000, 32000, 35000, 38000, 250000]
})

q1 = data["Salary"].quantile(0.25)
q3 = data["Salary"].quantile(0.75)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
```

---

# 🔎 8. Filtering Potential Outliers

```python
outliers = data[
    (data["Salary"] < lower_bound) |
    (data["Salary"] > upper_bound)
]

print(outliers)
```

This filters the observations that fall outside the IQR boundaries.

---

# 💼 9. Real-World Applications

## Business Analytics

IQR can help identify unusual:

* Employee salaries
* Transaction amounts
* Customer spending
* Delivery times
* Sales values

## AI / GenAI

IQR can be used to analyze:

* Model response latency
* Token usage
* API response times
* Evaluation scores
* Inference costs

# 📊 Day 37 — Variance

## 🚀 Data Science + Generative AI Learning Journey

# 📚 1. What Is Variance?

Variance measures the **average squared deviation of observations from the Mean**.

In simple terms:

> **Variance tells us how much the values vary around their Mean.**

### Basic Process

```text
Observation
     ↓
Difference from Mean
     ↓
Square the difference
     ↓
Average the squared differences
     ↓
Variance
```

---

# 📐 2. Understanding Deviation

A **deviation** tells us how far an observation is from the Mean.

### Formula

```text
Deviation = Observation - Mean
```

### Example

Consider:

```text
10, 20, 30
```

Mean:

```text
Mean = (10 + 20 + 30) / 3
     = 20
```

Deviations:

```text
10 - 20 = -10
20 - 20 =   0
30 - 20 = +10
```

So:

```text
Deviations = -10, 0, +10
```

---

# 📚 3. Why Do We Square Deviations?

If we simply add deviations, positive and negative values cancel each other.

For example:

```text
-10 + 0 + 10 = 0
```

That would incorrectly suggest there is no spread.

Therefore, we square the deviations:

```text
(-10)² = 100
(0)²   = 0
(10)²  = 100
```

Now:

```text
Squared deviations = 100, 0, 100
```

The values can no longer cancel each other.

---

# 🧮 4. Population Variance

Population variance is used when we have data for the **entire population** we are interested in.

### Formula

```text
σ² = Σ(x - μ)² / N
```

Where:

* `σ²` = Population Variance
* `x` = Individual observation
* `μ` = Population Mean
* `N` = Total number of observations

### Example

Consider:

```text
10, 20, 30
```

Mean:

```text
20
```

Squared deviations:

```text
100, 0, 100
```

Population Variance:

```text
Variance = (100 + 0 + 100) / 3
         = 200 / 3
         = 66.67
```

Therefore:

```text
Population Variance = 66.67
```

---

# 📊 5. Sample Variance

Sample variance is used when the data represents a **sample taken from a larger population**.

### Formula

```text
s² = Σ(x - x̄)² / (n - 1)
```

Where:

* `s²` = Sample Variance
* `x` = Individual observation
* `x̄` = Sample Mean
* `n` = Sample size

The important difference is:

```text
Population → divide by N
Sample     → divide by n - 1
```

---

# ❓ 6. Why Does Sample Variance Use n - 1?

When calculating variance from a sample, the sample Mean is itself estimated from the data.

Using `n - 1` instead of `n` provides an **unbiased estimate of the population variance** under the standard assumptions of random sampling.

This adjustment is known as **Bessel's correction**.

### Example

For:

```text
10, 20, 30
```

The squared deviations sum to:

```text
200
```

Sample Variance:

```text
200 / (3 - 1)
= 100
```

So:

```text
Population Variance = 66.67
Sample Variance     = 100
```

The two values are different because they answer different statistical questions.

---

# 🔍 7. Population vs Sample Variance

| Feature      | Population Variance       | Sample Variance              |
| ------------ | ------------------------- | ---------------------------- |
| Data         | Entire population         | Sample                       |
| Denominator  | `N`                       | `n - 1`                      |
| Symbol       | `σ²`                      | `s²`                         |
| Main purpose | Describe known population | Estimate population variance |

### Simple Example

If a company has salary data for **every employee**, population variance may be appropriate.

If we randomly select **100 employees** from a company with thousands of employees, sample variance is generally appropriate when estimating the population variability.

---

# 📈 8. Variance and Spread

A **higher variance** generally means observations are more spread out around the Mean.

A **lower variance** generally means observations are closer to the Mean.

### Example

Dataset A:

```text
48, 49, 50, 51, 52
```

Dataset B:

```text
10, 30, 50, 70, 90
```

Both have:

```text
Mean = 50
```

But Dataset B has much greater spread.

Therefore:

```text
Variance(B) > Variance(A)
```

### Important Insight

> **Two datasets can have the same Mean but very different variability.**

---

# ⚠️ 9. Variance Cannot Be Negative

Variance is calculated using **squared deviations**.

Since:

```text
(x - Mean)² ≥ 0
```

Variance cannot be negative.

Possible values are:

```text
Variance ≥ 0
```

If:

```text
Variance = 0
```

then every observation has the same value.

### Example

```text
50, 50, 50, 50
```

Mean:

```text
50
```

Every deviation is:

```text
0
```

Therefore:

```text
Variance = 0
```

---

# 📊 10. Variance vs IQR

Both Variance and IQR measure **spread**, but they behave differently.

| Measure  | What it measures                    | Outlier sensitivity |
| -------- | ----------------------------------- | ------------------- |
| Range    | Maximum − Minimum                   | Very high           |
| IQR      | Middle 50% spread                   | Low                 |
| Variance | Average squared deviation from Mean | High                |

### Key Difference

IQR focuses on the **middle 50%** of the data.

Variance uses **every observation** and squares its deviation from the Mean.

Therefore, extreme values can have a large effect on Variance.

### Example

```text
Dataset A:
10, 20, 30, 40, 50

Dataset B:
10, 20, 30, 40, 500
```

The extreme value `500` will substantially increase the Variance of Dataset B.

---

# 🐍 11. Variance Using NumPy

NumPy provides the `var()` function.

```python
import numpy as np

data = [10, 20, 30]

population_variance = np.var(data)

print("Population Variance:", population_variance)
```

Output:

```text
Population Variance: 66.66666666666667
```

### Sample Variance

NumPy uses `ddof=1` for the sample variance:

```python
sample_variance = np.var(data, ddof=1)

print("Sample Variance:", sample_variance)
```

Output:

```text
Sample Variance: 100.0
```

---

# 🐼 12. Variance Using Pandas

Pandas `var()` uses **sample variance by default**.

```python
import pandas as pd

data = pd.Series([10, 20, 30])

print(data.var())
```

Output:

```text
100.0
```

### Population Variance in Pandas

Use:

```python
data.var(ddof=0)
```

Output:

```text
66.66666666666667
```

### Important Difference

```text
NumPy np.var()
→ Population variance by default

Pandas Series.var()
→ Sample variance by default
```

This is an important detail to remember when working with real datasets.

---

# 💼 13. Business Application

Variance can help businesses understand how consistent or unstable a metric is.

### Example 1 — Daily Sales

Company A:

```text
1000, 1050, 1100, 950, 1020
```

Company B:

```text
500, 1500, 800, 2000, 300
```

Even if their average sales are similar, Company B has much greater variability.

Higher variance indicates that sales are less consistent.

### Example 2 — Customer Spending

Suppose two customer groups have the same average spending.

If Group A has low variance, customers spend relatively similar amounts.

If Group B has high variance, spending behavior is much more diverse.

This can influence:

* Customer segmentation
* Marketing strategies
* Pricing decisions
* Forecasting

# 📊 Day 38 — Standard Deviation, Z-Score & Standardization

# 📚 1. Standard Deviation

Standard Deviation is the **square root of Variance**.

## Formula

```text
Standard Deviation = √Variance
```

### Example

If:

```text
Variance = 25
```

Then:

```text
SD = √25
SD = 5
```

Therefore:

```text
Variance = 25
Standard Deviation = 5
```

---

# 🧠 2. Why Standard Deviation Is Useful

Variance is expressed in **squared units**.

For example:

```text
Salary → ₹
Variance → ₹²
```

Squared units are difficult to interpret directly.

Standard Deviation converts the measure back to the **original units**.

```text
Salary → ₹
Standard Deviation → ₹
```

Therefore Standard Deviation is usually easier to communicate and interpret.

---

# 📈 3. Standard Deviation and Spread

Consider two datasets.

### Dataset A

```text
48, 49, 50, 51, 52
```

The values are close to the Mean.

Therefore:

```text
Low Standard Deviation
```

### Dataset B

```text
10, 30, 50, 70, 90
```

The values are farther from the Mean.

Therefore:

```text
High Standard Deviation
```

### Key Relationship

```text
Low SD  → Less variability
High SD → More variability
```

---

# 📊 4. Variance vs Standard Deviation

| Feature        | Variance                   | Standard Deviation                      |
| -------------- | -------------------------- | --------------------------------------- |
| Measures       | Spread                     | Spread                                  |
| Calculation    | Average squared deviations | Square root of variance                 |
| Units          | Squared units              | Original units                          |
| Interpretation | More difficult             | Easier                                  |
| Used in        | Statistical calculations   | Statistical interpretation and analysis |

---

# 📐 5. Population vs Sample Standard Deviation

Just like Variance, Standard Deviation has Population and Sample versions.

### Population Standard Deviation

[
\sigma = \sqrt{\frac{\sum(x_i-\mu)^2}{N}}
]

### Sample Standard Deviation

[
s = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}
]

The main difference is the denominator:

```text
Population → N
Sample → n - 1
```

---

# 🧮 6. Standard Deviation Example

Dataset:

```text
2, 4, 6
```

From Day 37:

```text
Population Variance ≈ 2.67
```

Therefore:

```text
Population SD = √2.67
Population SD ≈ 1.63
```

So:

```text
Population Variance ≈ 2.67
Population Standard Deviation ≈ 1.63
```

---

# 📚 7. What Is a Z-Score?

A Z-Score tells us:

> **How many Standard Deviations an observation is above or below the Mean.**

## Formula

[
Z = \frac{x-\mu}{\sigma}
]

Where:

* `x` = individual observation
* `μ` = Mean
* `σ` = Standard Deviation

---

# 🧠 8. Z-Score Intuition

The formula can be understood as:

```text
Individual Value
      ↓
Subtract Mean
      ↓
Distance from Mean
      ↓
Divide by Standard Deviation
      ↓
Z-Score
```

So Z-Score expresses distance in **Standard Deviation units**.

---

# 🧮 9. Positive Z-Score Example

Suppose:

```text
Mean = 50
SD = 10
Value = 70
```

Then:

[
Z = \frac{70-50}{10}
]

[
Z = 2
]

Therefore:

```text
Z = +2
```

Interpretation:

> The value is **2 Standard Deviations above the Mean**.

---

# 🧮 10. Negative Z-Score Example

Suppose:

```text
Mean = 50
SD = 10
Value = 30
```

Then:

[
Z = \frac{30-50}{10}
]

[
Z = -2
]

Therefore:

```text
Z = -2
```

Interpretation:

> The value is **2 Standard Deviations below the Mean**.

---

# 📌 11. Z-Score Interpretation

```text
Z = 0
→ Exactly at the Mean

Z = +1
→ 1 SD above the Mean

Z = -1
→ 1 SD below the Mean

Z = +2
→ 2 SD above the Mean

Z = -2
→ 2 SD below the Mean

Z = +3
→ 3 SD above the Mean

Z = -3
→ 3 SD below the Mean
```

### Important Rule

```text
Positive Z → Above Mean
Negative Z → Below Mean
Zero Z → At Mean
```

The **absolute value** tells us how far the observation is from the Mean.

---

# 🧠 12. Why Z-Scores Are Useful

Suppose two different exams use different scoring scales.

### Mathematics

```text
Score = 80
Mean = 70
SD = 5
```

Z-Score:

```text
Z = (80 - 70) / 5
Z = 2
```

### Statistics

```text
Score = 90
Mean = 80
SD = 5
```

Z-Score:

```text
Z = (90 - 80) / 5
Z = 2
```

Raw scores are:

```text
80 and 90
```

but both students are:

```text
2 SD above their respective Means
```

Z-Scores therefore help compare observations relative to their own distributions.

---

# 🔄 13. Standardization

**Standardization** is the process of converting values into Z-Scores.

The formula is:

[
Z = \frac{x-\mu}{\sigma}
]

After standardization, the transformed data generally has:

```text
Mean ≈ 0
Standard Deviation ≈ 1
```

---

# 📊 14. Why Standardize Data?

Different features can have very different scales.

Example:

```text
Age:
18–60

Salary:
20,000–500,000

Experience:
0–30
```

These features have different numerical ranges.

Standardization converts them into a comparable scale.

This is useful for many Machine Learning algorithms where feature scale can affect the model or optimization process.

---

# ⚠️ 15. Standardization Does Not Remove Information

Standardization changes the **scale**, not the underlying observation relationship.

Example:

```text
Original value → Standardized value
140            → Z = 2
60             → Z = -2
```

The original values are still represented; they are simply expressed in standard deviation units.

---

# 🚨 16. Z-Scores and Potential Outliers

A commonly used screening rule is:

```text
|Z| > 3
```

This may indicate an unusually extreme observation.

Examples:

```text
Z = 0.8
→ Not particularly extreme

Z = -1.5
→ Relatively close

Z = 2.2
→ Relatively far

Z = 4.5
→ Potentially extreme
```

### Important

A large Z-Score does **not automatically mean the observation is an error**.

It only tells us that the observation is far from the Mean relative to the Standard Deviation.

---

# 🔢 17. NumPy — Standard Deviation

```python
import numpy as np

values = np.array([10, 20, 30, 40, 50])

population_sd = np.std(values)
sample_sd = np.std(values, ddof=1)

print("Population SD:", population_sd)
print("Sample SD:", sample_sd)
```

### Important

```python
np.std(values)
```

uses Population Standard Deviation by default.

For Sample Standard Deviation:

```python
np.std(values, ddof=1)
```

---

# 🐼 18. Pandas — Standard Deviation

```python
import pandas as pd

values = pd.Series([10, 20, 30, 40, 50])

population_sd = values.std(ddof=0)
sample_sd = values.std()

print("Population SD:", population_sd)
print("Sample SD:", sample_sd)
```

### Important

Pandas:

```python
values.std()
```

uses Sample Standard Deviation by default.

Population Standard Deviation:

```python
values.std(ddof=0)
```

---

# 🔢 19. NumPy — Z-Scores

```python
import numpy as np

values = np.array([10, 20, 30, 40, 50])

mean = np.mean(values)
sd = np.std(values)

z_scores = (values - mean) / sd

print("Mean:", mean)
print("Standard Deviation:", sd)
print("Z-Scores:", z_scores)
```

The expression:

```python
(values - mean) / sd
```

calculates a Z-Score for every value.

This is an example of **NumPy vectorized computation**.

---

# 🐼 20. Pandas — Standardization

```python
import pandas as pd

values = pd.Series([10, 20, 30, 40, 50])

mean = values.mean()
std = values.std(ddof=0)

standardized_data = (values - mean) / std

print("Original Data:")
print(values)

print("\nStandardized Data:")
print(standardized_data)
```

Expected standardized values are approximately:

```text
-1.414
-0.707
 0.000
 0.707
 1.414
```

The value `30` has:

```text
Z = 0
```

because it is exactly equal to the Mean.

---

# 🧪 21. Mini Data Science Challenge

A dataset contains student marks:

```python
import pandas as pd

data = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Math": [60, 70, 80, 90, 100],
    "Statistics": [50, 65, 75, 85, 95]
})
```

The task was to calculate:

* Mean Math score
* Mean Statistics score
* Population SD for Math
* Population SD for Statistics
* Math Z-Scores
* Statistics Z-Scores

### Z-Score columns

```python
data["Math_Z"] = (
    data["Math"] - data["Math"].mean()
) / data["Math"].std(ddof=0)

data["Stats_Z"] = (
    data["Statistics"] - data["Statistics"].mean()
) / data["Statistics"].std(ddof=0)
```

---

# 📊 22. Mini Challenge Interpretation

The highest Math score belongs to:

```text
Student E
```

The highest Statistics score belongs to:

```text
Student E
```

However, a raw score alone is not always enough to compare performance across different distributions.

Z-Scores provide a way to compare performance relative to each distribution.

# 📊 Day 39 — Skewness, Distribution Shape & Descriptive Statistics Case Study

# 📚 1. Distribution Shapes

### Symmetric Distribution

```text
        /\
       /  \
      /    \
_____/      \_____
```

```text
Mean ≈ Median
```

The distribution has approximately balanced tails.

---

### Right-Skewed Distribution

```text
        /\
       /  \
      /    \
_____/      \____________
```

```text
Mean > Median
```

The distribution has a longer tail toward larger values.

**Examples:**

* Income
* Customer spending
* House prices

---

### Left-Skewed Distribution

```text
_____________/\
            /  \
           /    \
__________/      \____
```

```text
Mean < Median
```

The distribution has a longer tail toward smaller values.

---

# 🚨 2. Skewness vs Outlier

| Concept      | Meaning                              |
| ------------ | ------------------------------------ |
| **Skewness** | Shape or asymmetry of a distribution |
| **Outlier**  | Unusually extreme observation        |

An outlier can contribute to skewness, but an outlier is **not automatically an error**.

---

# 📊 3. Customer Spending Case Study

### Dataset

```text
₹500, ₹550, ₹600, ₹620, ₹650,
₹700, ₹750, ₹800, ₹900, ₹3,000
```

### Descriptive Statistics

| Statistic                     |     Value |
| ----------------------------- | --------: |
| Mean                          |      ₹907 |
| Median (Q2)                   |      ₹675 |
| Q1                            |      ₹600 |
| Q3                            |      ₹800 |
| IQR                           |      ₹200 |
| Lower Bound                   |      ₹300 |
| Upper Bound                   |    ₹1,100 |
| Range                         |    ₹2,500 |
| Population Variance           | ≈ 510,210 |
| Population Standard Deviation |    ≈ ₹714 |
| Z-Score of ₹3,000             |    ≈ 2.93 |

---

# 🔍 4. Outlier Analysis

Using the **1.5 × IQR rule**:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Therefore:

```text
Lower Bound = ₹600 - (1.5 × ₹200)
            = ₹300
```

```text
Upper Bound = ₹800 + (1.5 × ₹200)
            = ₹1,100
```

Since:

```text
₹3,000 > ₹1,100
```

₹3,000 is identified as a **potential outlier**.

---

# 📈 5. Distribution Interpretation

The dataset is **right-skewed** because the ₹3,000 transaction creates a long right tail.

```text
Mean   = ₹907
Median = ₹675

Mean > Median
```

The Mean being substantially greater than the Median supports the interpretation that the distribution is right-skewed.

---

# 💼 6. Business Interpretation

The ₹3,000 transaction pulls the Mean upward.

Therefore, the **Median of ₹675** provides a better representation of typical customer spending for this dataset.

However, the transaction should **not automatically be removed**.

If ₹3,000 represents a genuine bulk purchase, it is valid business data and should be retained.

A better approach is to investigate the transaction and determine why it is unusually high.

### Possible explanations

* Bulk purchase
* High-value customer
* Special order
* Business customer
* Data-entry error
* Fraudulent transaction

# 🎲 Day 40 — Probability Fundamentals

## 🚀 Data Science Learning Journey

**Phase:** Mathematics for Data Science
**Module:** Probability
**Day:** 40
**Topic:** Probability Fundamentals, Probability Rules & Conditional Probability
**Status:** ✅ Completed
**Environment:** Jupyter Notebook

---

## 📌 Overview

Day 40 marked the beginning of the **Probability** module.

The focus was on understanding the fundamentals of probability, learning basic probability rules, and applying **conditional probability** to practical customer data.

The day followed this progression:

```text
Probability Fundamentals
        ↓
Probability Rules
        ↓
Conditional Probability
        ↓
NumPy + Pandas
        ↓
Business Interpretation
```

---

## 🎯 Learning Objectives

By the end of Day 40, I learned how to:

* Understand the meaning of probability.
* Understand experiments, outcomes, and events.
* Calculate basic probabilities.
* Understand the probability range.
* Apply the complement rule.
* Apply the addition rule.
* Understand mutually exclusive events.
* Understand conditional probability.
* Calculate conditional probabilities from data.
* Use NumPy and Pandas for probability analysis.
* Interpret probability in a business context.

---

# 📚 1. What Is Probability?

**Probability** measures how likely an event is to occur.

The probability of an event is always between **0 and 1**.

```text
0 ≤ P(A) ≤ 1
```

Where:

* `P(A) = 0` → Event is impossible
* `P(A) = 1` → Event is certain
* Values between 0 and 1 → Different levels of likelihood

### Example

If a customer has a 70% probability of purchasing:

```text
P(Purchase) = 0.70
```

---

# 🎲 2. Experiment, Outcome & Event

### Experiment

A process that produces an outcome.

Example:

```text
Rolling a die
```

### Outcome

A possible result of an experiment.

```text
1, 2, 3, 4, 5, 6
```

### Event

A collection of one or more outcomes.

Example:

```text
Rolling an even number
```

Event:

```text
{2, 4, 6}
```

---

# 📊 3. Basic Probability Formula

For equally likely outcomes:

```text
P(A) = Favorable Outcomes / Total Outcomes
```

### Example

For a fair die, probability of rolling an even number:

```text
Favorable outcomes = 3
Total outcomes = 6

P(Even) = 3 / 6
        = 0.5
```

Therefore:

```text
P(Even) = 50%
```

---

# 🔄 4. Complement Rule

The complement of an event means the event **does not occur**.

### Formula

```text
P(Aᶜ) = 1 - P(A)
```

### Example

If:

```text
P(Purchase) = 0.70
```

Then:

```text
P(No Purchase) = 1 - 0.70
               = 0.30
```

Therefore:

```text
P(No Purchase) = 30%
```

---

# ➕ 5. Addition Rule

The addition rule is used to calculate the probability of **A or B**.

For mutually exclusive events:

```text
P(A ∪ B) = P(A) + P(B)
```

### Example

Suppose:

```text
P(Red) = 0.30
P(Blue) = 0.20
```

If the events are mutually exclusive:

```text
P(Red or Blue) = 0.30 + 0.20
               = 0.50
```

---

# 🚫 6. Mutually Exclusive Events

Two events are **mutually exclusive** when they cannot occur at the same time.

### Example 1

A single die roll cannot be both:

```text
2 and 5
```

### Example 2

A customer cannot be classified as both:

```text
New Customer
and
Existing Customer
```

when those categories are defined as mutually exclusive.

---

# 🔀 7. Conditional Probability

Conditional probability measures the probability of an event **given that another event has already occurred**.

Where:

* `A` = Event of interest
* `B` = Given condition
* `A ∩ B` = Both A and B occur

### Key Idea

> **Conditional probability changes the reference group.**

Instead of asking:

```text
What is the probability that a customer purchases?
```

we might ask:

```text
What is the probability that a customer purchases
given that they are a mobile user?
```

---

# 👥 8. Customer Dataset Example

Suppose we have:

| Customer Type | Purchased | Count |
| ------------- | --------- | ----: |
| Mobile        | Yes       |    60 |
| Mobile        | No        |    40 |
| Desktop       | Yes       |    30 |
| Desktop       | No        |    70 |

Total customers:

```text
200
```

Overall purchase probability:

```text
P(Purchase) = 90 / 200
            = 0.45
```

So:

```text
P(Purchase) = 45%
```

---

# 📱 9. Conditional Probability Example

Now consider only **mobile users**.

There are:

```text
60 + 40 = 100 mobile users
```

Among them:

```text
60 purchased
```

Therefore:

```text
P(Purchase | Mobile)
= 60 / 100
= 0.60
```

So:

```text
P(Purchase | Mobile) = 60%
```

Compare:

```text
Overall Purchase Probability = 45%

Purchase Probability | Mobile = 60%
```

This suggests mobile users have a higher observed purchase rate in this dataset.

---

# 🐍 10. Probability Using NumPy

```python
import numpy as np

purchased = np.array([1, 1, 1, 0, 0, 1, 0, 1])

probability = np.mean(purchased)

print("Probability of Purchase:", probability)
```

Since the data uses:

```text
1 = Purchased
0 = Not Purchased
```

the mean represents the proportion of customers who purchased.

---

# 🐼 11. Probability Using Pandas

```python
import pandas as pd

data = pd.DataFrame({
    "Mobile_User": ["Yes", "Yes", "No", "Yes", "No", "Yes"],
    "Purchased": [1, 1, 0, 1, 0, 0]
})

purchase_rate = data["Purchased"].mean()

print("Overall Purchase Probability:", purchase_rate)
```

### Conditional Probability

```python
mobile_users = data[data["Mobile_User"] == "Yes"]

mobile_purchase_probability = mobile_users["Purchased"].mean()

print("Purchase Probability | Mobile:",
      mobile_purchase_probability)
```

---

# 💼 12. Business Interpretation

Probability allows businesses to reason about uncertainty and customer behavior.

For example:

```text
P(Purchase) = 45%
P(Purchase | Mobile) = 60%
```

The observed purchase rate is higher among mobile users.

A business could investigate whether:

* Mobile users respond better to promotions.
* The mobile experience is better optimized.
* Mobile users have different purchasing behavior.
* A mobile-specific campaign could improve conversions.

**Important:** A higher conditional probability shows an association in the observed data. It does **not automatically prove that being a mobile user causes the purchase.**

---

# 🧠 13. Key Data Science Lessons

* Probability measures the likelihood of an event.
* Probability ranges from `0` to `1`.
* The complement rule calculates the probability of an event not occurring.
* Addition rules help calculate probabilities involving multiple events.
* Mutually exclusive events cannot happen simultaneously.
* Conditional probability considers additional information.
* Conditional probability changes the population being analyzed.
* Pandas can calculate probabilities using proportions and group filtering.
* Probability helps quantify uncertainty in business and data science.
* A probability relationship does not automatically imply causation.

---

# 🔑 Key Formulas

### Basic Probability

```text
P(A) = Favorable Outcomes / Total Outcomes
```

### Complement Rule

```text
P(Aᶜ) = 1 - P(A)
```

### Mutually Exclusive Addition Rule

```text
P(A ∪ B) = P(A) + P(B)
```

### Conditional Probability

```text
P(A|B) = P(A ∩ B) / P(B)
```

---

# 🚀 Day 40 Status

**Completed:** ✅

### Skills Practiced

```text
Probability
    ↓
Probability Rules
    ↓
Complement
    ↓
Mutually Exclusive Events
    ↓
Conditional Probability
    ↓
NumPy + Pandas
    ↓
Business Interpretation
```

**Next:** Continue with the next topic in the Probability module.

# 👨‍💻 Author

**Siva Kumar Reddy**

📊 Aspiring AI/Data Scientist  
🚀 Building projects daily

---







