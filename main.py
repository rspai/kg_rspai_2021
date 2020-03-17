"""
@author: Rasita Pai
Q: to check whether a one-to-one character mapping exists from one string, s1, to another string, s2.
"""


import sys


def IsMapped(str1, str2):
    if len(str1) == len(str2):
        for char in str1:
            if str1.count(char) > 1:
                return 0
        return 1
    else:
        return 0    
        
s1 = sys.argv[1]
s2 = sys.argv[2]        
# print('str1: ', s1)
# print('str2: ', s2)
print(bool(IsMapped(s1, s2)))