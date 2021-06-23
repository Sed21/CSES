"""
Time limit: 1.00 s Memory limit: 512 MB
You are given a list of n integers, and your task is to calculate the number of distinct values in the list.

Input

The first input line has an integer n: the number of values.

The second line has n integers x1,x2,…,xn.

Output

Print one integers: the number of distinct values.

Constraints
1≤n≤2⋅105
1≤xi≤109
Example

Input:
5
2 3 2 2 3

Output:
2

Source = https://cses.fi/problemset/task/1621
"""

import sys
def readarray(): return list(map(int, sys.stdin.readline().split()))

def distinct_numbers(array: [int]):
    return len(set(array))

readarray()
print(distinct_numbers(readarray()))
