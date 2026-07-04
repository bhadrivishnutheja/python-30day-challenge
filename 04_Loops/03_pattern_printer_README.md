# 03_pattern_printer.py - Simple Explanation

## What this program does
This program prints different shapes using stars and numbers.

It shows:
- a right triangle
- an inverted triangle
- a pyramid
- a number pattern

## How it works
The program uses loops to repeat printing.

Each row is printed one by one.

### Example
For a triangle:
- first row prints 1 star
- second row prints 2 stars
- third row prints 3 stars
- and so on

## Very simple way to understand it
Think of it like drawing row by row.

The program says:
- draw one star
- then draw two stars
- then three stars
- keep going until the last row

## How the solution is made
The program uses loops in a smart way:
- one loop controls the row number
- another loop may control how many stars or spaces to print

So the shape is built step by step.

## Program logic: how the program solves the problem
This program solves the problem by drawing one row at a time.

1. It asks for how many rows the pattern should have.
2. It starts from the first row.
3. For each row, it decides how many stars or numbers to print.
4. It prints that row.
5. It moves to the next row and repeats the same idea.

For the triangle, the number of stars grows.
For the inverted triangle, the number of stars shrinks.
For the pyramid, it adds spaces and stars to make the shape look centered.
For the number pattern, it prints numbers in increasing order row by row.

So the program solves the problem by following a simple rule again and again until the full shape is complete.

## What each pattern means
- Right triangle: grows from small to big
- Inverted triangle: starts big and becomes small
- Pyramid: has spaces on the left and stars in the middle
- Number pattern: prints numbers in increasing order row by row

## How to run it
Use this command:

```bash
python3 03_pattern_printer.py
```

## Easy summary
This program is like a drawing machine. It repeats simple instructions to make beautiful shapes.
