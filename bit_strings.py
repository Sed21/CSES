"""
Time limit: 1.00 s Memory limit: 512 MB
Your task is to calculate the number of bit strings of length n.

For example, if n=3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.

Input

The only input line has an integer n.

Output

Print the result modulo 10^9+7.

Constraints
1≤n≤106
Example

Input:
3

Output:
8

Source = https://cses.fi/problemset/task/1617
"""
import sys
def readint(): return int(sys.stdin.readline())

def bit_strings(n: int):
    result = 1
    exp = 1
    modulo = int(1e9 + 7)

    while n >= 1:
        result = ((result % modulo) * 2) % modulo
        n -= 1
    return result

print(bit_strings(readint()))
