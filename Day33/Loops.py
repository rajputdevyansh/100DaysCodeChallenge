"""
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print.
Example
The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
Input Format
The first and only line contains the integer
Output Format
Print  lines, one corresponding to each .
"""
n = int(input())
for i in range(0,n):
    print(i**2)
"""
Compiler Message
Success
Input (stdin)
5
Expected Output
0
1
4
9
16
"""
