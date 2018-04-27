import os, time, sys
import random

l1=range(100000)
random.shuffle(l1)
f=open("data.txt", "r") #open the file for Read.
x=f.read().splitlines() #this returns a list of strings.
for i in range(len(x)):
  x[i]=int(x[i])        #convert the elements to integer
f.close()
#l2 = [1,2,3,4,5,6,4,3,1,345,456,567,234,213,34,567,678,3,123,13]
#l=[6,3]
def bubblesort(l):
  for i in range(len(l)):
    for j in range((len(l)-i-1)):
    #after every iteration, last i items in the list are in their right positions.
      if l[j]>l[j+1]:
        l[j], l[j+1]=l[j+1], l[j] #swap the two
  return l

if __name__=='__main__':
  t1=time.time()
#  print l2
  res=bubblesort(x)
#  print res
  t2=time.time()
  print t2-t1
