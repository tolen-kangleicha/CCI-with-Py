"""
Given a string S, check if characters of the given string can be rearranged to form a palindrome.

Input: Codingcoding
Output: Yes
"""
from collections import Counter

def palin(S):
    freq = Counter(S.lower()) 
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    return "Yes" if odd_count <= 1 else "No"

print(palin("Codingcoding"))
