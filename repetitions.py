"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3

Source = https://cses.fi/problemset/task/1069
"""

def repetitions(seq: str):
    last_ch = seq[0]
    curr = 0
    max_seq = 1

    for ch in seq:
        if last_ch != ch:
            if max_seq < curr: max_seq = curr
            curr = 1
            last_ch = ch
        else:
            curr += 1
    if max_seq < curr: max_seq = curr
    return max_seq    

print(repetitions(input()))