#! /usr/bin/env python3

def area(l, b):
    print(l*b)

area(10,20)

#function with default values for parameters

def area1(l=20,b=30):
    print(l*b)

#making the function call without arguments
area1()
#making the function call with arguments
area1(40,50)

