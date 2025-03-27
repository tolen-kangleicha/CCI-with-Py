"""
Given a string S and text T, print the smallest window in the string S having all characters of the text T. Both the string S and text T contains lowercase english alphabets.

Input: timetopractice   toc 
Output: toprac
"""

def sub_str(S, T):
    beg_ch, end_ch = T[0], T[-1]
    for ch in S:
        if ch == beg_ch:
            print(ch, end="")
