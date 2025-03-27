"""
Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.

Input: zxvczbtxyzvy
Output: c
"""

def find(S):
    freq = {}
    for ch in S:
        freq[ch] = freq.get(ch, 0) + 1
    
    for ch in S:
        if freq[ch] == 1:
            return ch
    return None 

print(find("zxvczbtxyzvy"))
