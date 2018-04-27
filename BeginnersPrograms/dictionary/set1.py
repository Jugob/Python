#! /usr/bin/env python3

s1= {"a","b","c","d","e"}
s2= {"d","e","f","g","h"}

#union of two sets
print("Union of sets s1 and s2:\n{}\n".format(s1.union(s2)))

#intersection of two sets
print("Intersection of sets s1 and s2:\n{}\n".format(s1.intersection(s2)))

#difference of two sets
print("Difference of sets s1-s2 :\n{}\n".format(s1-s2))

#difference of two sets
print("Difference of sets s2-s1 :\n{}\n".format(s2-s1))

#symmetric difference between 2 sets
print("Symmetric difference between s1 and s2:\n{}\n".format(s1^s2))
