#! /usr/bin/env python3

def positions(a,b,c=3,d=4):
    return a+b+c+d

p1 = positions(5,6,d=7)
print("p1={}".format(p1))

p2=positions(a=5, d=2, b=4, c=6)
print("p2={}".format(p2))

