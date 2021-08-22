#!/usr/bin/env python

# Comparisons:
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=
# Object Identity: is

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))
