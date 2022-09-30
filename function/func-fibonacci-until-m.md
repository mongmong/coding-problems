# Loop - Fibonacci Until M

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

Given m (m >= 0), print all Fibonacci numbers that are less than or equal to m.

## Hints

Write the Fib(n) function to find the nth number in the Fibonacci sequence.

Write a loop to call the Fib(n) to find the nth Fibonacci number and print if it is less than or equal to m.

## Example

Input:

    m = 14

Output:

    0, 1, 1, 2, 3, 5, 8, 13