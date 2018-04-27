#!/usr/bin/env python3

#split
str1="In the face of ambiguity, refuse the temptation to guess."
sp1=str1.split(" ") #split takes a delimiter as an argument
print("type of data sp1 is: {}".format(type(sp1)))
print("sp1={}".format(sp1))

#using "the" as delimiter
sp2=str1.split("the")
print("sp2={}".format(sp2))

#join
j1=" ".join(sp1)
print("Joined string j1={}".format(j1))

#join() is just the reverse of split()

j2="the".join(sp2)
print("Joined string j2={}".format(j2))

str2= "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts."

print("str2={}".format(str2))
print("\n")
sp3=str2.split("\n")
print("sp3={}".format(sp3))

sp4=str2.split(".")
print("sp4={}".format(sp4))

#strip()
print("sp4[1]={}".format(sp4[1]))#note that there is a newline char at the start

print("sp4[1] with no extra character is: {}".format(sp4[1].strip()))
