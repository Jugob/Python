#! /usr/bin/env python3

def variadic(*args):
    print(type(args))
    for i in args:
        print(i)

#calling the function
variadic(5,4,3,2,1)
variadic(5,4,3,2)
variadic(5)
