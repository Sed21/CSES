"""
Time limit: 1.00 s Memory limit: 512 MB
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.

Constraints
2≤n≤2⋅10^5
Example

Input:
5
2 3 1 5

Output:
4

Source = https://cses.fi/problemset/task/1083
"""

import sys

def readarray(): return list(map(int, sys.stdin.readline().split()))

def missing_number(array: [int], n: int):
    sum_all = n * (n + 1) // 2
    sum_arr = sum(array)
    return sum_all - sum_arr

n = readarray()[0] 
print(missing_number(readarray(), n)) 
