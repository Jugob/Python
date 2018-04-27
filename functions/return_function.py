#! /usr/bin/env python3

#a fcuntion that does not return anything. It just prints a value.
def area(l,b):
    print(l*b)


#a fcuntion that returns a value.
def area1(l,b):
    return l*b

#a function that has a return statement but no value is returned.
def area2(l,b):
    print(l*b)
    return

# making function calls:
print("function area()")
area(5,10)
print("function area1()")
a=area1(5,10)
print(a)
print("function area2()")
a1=area2(5,10)
print(a1)
