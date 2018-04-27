#! /usr/bin/env python3

def kwargs_fun(**kwargs):
    print(type(kwargs))
    for i in kwargs.keys():
        print(kwargs[i])


kwargs_fun(a=1,b=2,c=3)
