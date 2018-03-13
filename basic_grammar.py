#!/usr/bin/env python
# file:basic_grammar.py
# this is basic grammar for python

# 1.indentation
if True:
    print("it is true")
else:
    print("it is fault")
# note: it need to use the same indentation

# multi-line
a = 1
b = 1
c = a + \
    b

# string should be start and end with the same character (') or (") or (""")
day = {'MON', "TUS", """WED"""}
days = {'MON', "TUS", """WED"""}
week = {'MON', "TUS", """WED"""}

# multi-line comment
'''
multi-line comment
'''

"""
multi-line comment
"""

# multi-statement
import sys; x = "ming"; sys.stdout.write(x + '\n')

# line output
x = "hello"
y = "ming"
print(x)
print(y)
print("----------")
# this should output to one line
print(x),
print(y),
