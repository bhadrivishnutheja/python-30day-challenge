# 01_multiplication.py - Simple Explanation

## What this program does
This program asks you for a number and a limit, then prints the multiplication table for that number.

Example:
- If you enter 3 and 5, it will show:
  - 3 x 1 = 3
  - 3 x 2 = 6
  - 3 x 3 = 9
  - 3 x 4 = 12
  - 3 x 5 = 15

## How it works
Think of this program like a teacher writing the table of a number one line at a time.

1. It asks for a number.
2. It asks for how many times you want to multiply it.
3. It uses a loop to repeat the multiplication again and again.
4. Each time, it prints the answer.

## Very simple way to understand it
Imagine you have a number, for example 4.
You want to say:
- 4 times 1
- 4 times 2
- 4 times 3
- and so on

The program does this automatically for you.

## How the solution is made
The main idea is:
- start from 1
- keep going until the limit is reached
- each time multiply the chosen number by the current number

So it is just repeating the same small job many times.

## Program logic: how the program solves the problem
This program solves the problem by breaking it into tiny steps.

1. It takes the number the user wants to multiply.
2. It takes the maximum number of times to multiply it.
3. It starts from 1 and keeps increasing by 1.
4. For each value, it calculates:
   - chosen number x current value
5. It prints the result on the screen.
6. It stops when the loop reaches the limit.

In simple words, the program is saying: "Do the same multiplication again and again, but change the number each time."

## How to run it
Open the terminal and go to the folder where the file is saved.
Then run:

```bash
python3 01_multiplication.py
```

## Easy summary
This program is just a smart calculator that prints multiplication results again and again.
