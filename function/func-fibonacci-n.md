# Loop - Fibonacci N

## Problem

Fibonacci sequence is a series of non-negative numbers starting with 0 and 1:

    0, 1, 1, 2, 3, 5, 8, ...

The Fibonacci function Fib(n) can be defined as following to return the nth number in the Fibonacci sequence.

```
Fib(n) = 
    Fib(n - 1) + Fib(n - 2)     # if n >= 3
    1                           # if n == 2
    0                           # if n == 1
```

Given n (n >= 1), print the first n numbers in the Fibonacci sequence.

## Hints

Write the Fib(n) function to find the nth number in the Fibonacci sequence.

Write a for loop to call the Fib(n) function to print the first n numbers.

## Example

Input:

    n = 8

Output:

    0, 1, 1, 2, 3, 5, 8, 13