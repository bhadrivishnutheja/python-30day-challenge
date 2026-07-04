# Loops in Python for Beginners

## What is a loop?
A loop is a way to repeat something again and again without writing the same code many times.

Think of it like this:
- You want to say hello 5 times.
- Instead of writing hello 5 times, you use a loop.

## Why do we use loops?
Loops are used when you want to:
- repeat a task many times
- go through a list of items
- print patterns
- do calculations again and again

## Types of loops in Python
Python has mainly two common loops:

1. for loop
2. while loop

## 1. for loop
A for loop is used when you know how many times you want to repeat something.

### Example
```python
for i in range(5):
    print(i)
```

### What this does
It prints numbers from 0 to 4.

### Simple explanation
It says:
- start from 0
- keep going until 4
- print each number

## 2. while loop
A while loop keeps repeating as long as a condition is true.

### Example
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### What this does
It prints numbers from 1 to 5.

### Simple explanation
It keeps repeating until the condition becomes false.

## Loop concepts you should know

### 1. range()
The range() function helps you create a sequence of numbers.

Example:
```python
range(5)
```
This gives numbers 0, 1, 2, 3, 4.

### 2. break
break stops the loop immediately.

Example:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### 3. continue
continue skips the current step and goes to the next one.

Example:
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

## Common beginner loop programs
In this folder, you will learn loops through these programs:

- multiplication table program
- sum of numbers program
- pattern printing program

## How loops help in these programs

### Multiplication table
A loop repeats the multiplication again and again.

### Sum of numbers
A loop adds numbers one by one.

### Pattern printing
A loop prints rows and stars again and again to make shapes.

## Very simple way to think about loops
A loop is like a robot that repeats the same task.

Example:
- “Print 1”
- “Print 2”
- “Print 3”

The loop does this automatically.

## Easy summary
Loops are used to repeat work again and again.
They make programs shorter and smarter.

If you know how to use loops, you can solve many beginner problems easily.

## Practice ideas
Try these on your own:
- print numbers from 1 to 10
- print even numbers
- print odd numbers
- print a square pattern
- find the sum of first 10 numbers
