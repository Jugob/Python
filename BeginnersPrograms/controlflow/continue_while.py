#!/usr/bin/env python3

#example with while loop
n=1
while n<15:
    if n%3==0:
        n+=1
        continue
    print(n*n*n)
    n+=1
