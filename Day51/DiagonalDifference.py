"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
Function description
Complete the  function in the editor below.
diagonalDifference takes the following parameter:
int arr[n][m]: an array of integers
Return
int: the absolute diagonal difference

Input Format
The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
"""
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    a=0
    b=0
    for i in range(len(arr[0])):
        a += arr[i][i]
        b += arr[i][(len(arr[0]))-i-1]
    return abs(a-b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
Compiler Message
Success
Input (stdin)

3
11 2 4
4 5 6
10 8 -12
Expected Output

15
"""
