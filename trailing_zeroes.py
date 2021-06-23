"""
Your task is to calculate the number of trailing zeros in the factorial n!.

For example, 20!=2432902008176640000 and it has 4 trailing zeros.

Input

The only input line has an integer n.

Output

Print the number of trailing zeros in n!.

Constraints
1≤n≤109
Example

Input:
20

Output:
4

Source = https://cses.fi/problemset/task/1618
"""

def trailings_zeroes(n: int):
    div = 5
    count = 0

    while n // div >= 1:
        count += n // div
        div *= 5
    return count

print(trailings_zeroes(int(input())))
