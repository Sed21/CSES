"""
Time limit: 1.00 s Memory limit: 512 MB
Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input

The only input line has a string of length n consisting of characters A–Z.

Output

Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106
Example

Input:
AAAACACBA

Output:
AACABACAA

Source = https://cses.fi/problemset/task/1755
"""
from collections import Counter
def palidrom_reoder(string: str):
    stru = Counter(string)
    if len(string) == 1: 
        print(string)
        return
    if len(list(filter(lambda x: x % 2 == 1, stru.values()))) > 1:
        print("NO SOLUTION")
        return

    limit = sum(stru.values()) 
    palidrom = [''] * limit
    offset = 0
    last = None

    for key in stru.keys():
        num = stru.get(key)
        if(num % 2 == 1 or num == 1): 
            last = key
            continue
        num //= 2
        for i in range(num):
            palidrom[i + offset], palidrom[limit - i - offset - 1] = key, key
        offset += num

    if last:
        if stru.get(last):
            palidrom.insert(limit // 2, last)
        else :
            for i in range(stru.get(last)):
                palidrom[i + offset], palidrom[limit - i - offset - 1] = last, last
    print(''.join(palidrom))

palidrom_reoder(input())
