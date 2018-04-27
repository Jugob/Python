#!/usr/bin/env python3

str1="If the implementation is hard to explain, it's a bad idea."

str2=str1[7:22]  #giving the start and end as input
print("str2 is: {}".format(str2))

str3=str1[7:22:2]   # giving start, end and step-size as parameters.
print("Str3 is: {}".format(str3))

str4=str1[:len(str1)-1]    # start position is left blank, default 0
print("Str4 is: {}".format(str4))

str5=str1[:len(str1)-1:2] # start at 0(default), step-size=2
print("Str5 is: {}".format(str5))

str6=str1[10:] # start at 0, end at end(default), step-size=1(default)
print("Str6 is: {}".format(str6))

str7=str1[10::3] #start 10, end default, step-size=3
print("Str7 is: {}".format(str7))

str8=str1[::] #start, end and step-size all default
print("Str8 is: {}".format(str8))





print
