"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Function Description

Complete the plusMinus function in the editor below.
plusMinus has the following parameter(s):
int arr[n]: an array of integers

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe.

Output Format

Print the following  lines, each to  decimals:
proportion of positive values
proportion of negative values
proportion of zeros
"""
import math
import os
import random
import re
import sys


def plusMinus(arr):
    p=0
    n=0
    a=0
    for i in range(len(arr)):
        if(arr[i]>0):
            p+=1
        elif(arr[i]==0):
            a+=1
        else:
            n+=1
    print(p/len(arr))
    print(n/len(arr))
    print(a/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
"""
Compiler Message
Success
Input (stdin)

6
-4 3 -9 0 4 1
Expected Output

0.500000
0.333333
0.166667
"""
