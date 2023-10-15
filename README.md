## Problem Statement

You are tasked with writing a Python program that generates the first N numbers in the Fibonacci sequence without utilizing any custom functions. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

**Write a program that generates and print the first N numbers in the Fibonacci sequence.**

### Input

- `N`: An integer representing the number of Fibonacci numbers to generate where `N >= 0`.

### Output

- print the first N numbers in the Fibonacci sequence, separated by commas ","
## Fibonacci Sequence Explanation

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. It usually starts with 0 and 1. The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on, where each number is the sum of the two preceding ones before it.

The Fibonacci sequence can be represented by the following recurrence relation:
\[F(n) = F(n-1) + F(n-2)\]
with seed values \(F(0) = 0\) and \(F(1) = 1\).

## Example

```python
1. **Case where N is 0:**
   - Input: N = 0
   - Output: ""
   - Explanation: When N is 0, there are no numbers in the Fibonacci sequence.

2. **Case where N is 1:**
   - Input: N = 1
   - Output: "0"
   - Explanation: The first number in the Fibonacci sequence when N is 1 is 0.

3. **Case where N is 2:**
   - Input: N = 2
   - Output: "0,1"
   - Explanation: The first two numbers in the Fibonacci sequence are 0 and 1.

4. **Case where N is 5:**
   - Input: N = 5
   - Output: "0,1,1,2,3"
   - Explanation: The first five numbers in the Fibonacci sequence are 0, 1, 1, 2, and 3.

5. **Case where N is 10:**
   - Input: N = 10
   - Output: "0,1,1,2,3,5,8,13,21,34"
   - Explanation: The first ten numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
