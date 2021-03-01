import os,sys
sys.path.insert(1, os.path.abspath(os.path.dirname(__file__)))

def add1(a,b):
    print(a+b)

l1 = ['a', 'b', 'c', 'd', 'e']
s = "".join(l1)

print(s)
print(s.isalnum())
print(s.isdigit())
print(s.isalpha())
print("\n")

s = "12345abcde"
print(s)
print(s.isalnum())
print(s.isdigit())
print(s.isalpha())



"""
Can you try this in player.py
import sys
sys.path.insert(1, os.path.abspath(os.path.dirname(__file__)))
"""

