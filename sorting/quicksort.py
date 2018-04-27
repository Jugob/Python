import os, time, sys

#l1 = [1,2,3,4,5,6,4,3,1,345,456,567,234,213,34,567,678,3,123,13]
#l=[6,3]
#print l1

f=open("data.txt", "r")
x=f.read().splitlines()
for i in range(len(x)):
 x[i]=int(x[i])
f.close()


def partition(l, start, end):
  pivot=l[end]
  bottom=start-1
  top = end
  
  done=0
  while not done:
    while not done:
      bottom+=1
      
      if bottom==top:
        done=1
        break
      
      if l[bottom]>pivot:
        l[top]=l[bottom]
        break

    while not done:
      top -=1
      
      if top==bottom:
        done =1
        break


      if l[top]<pivot:
        l[bottom]=l[top]
        break

  l[top]=pivot
  return top

def quicksort(l, start, end):
  if start<end:
    split=partition(l, start, end)
    quicksort(l, start, split-1)
    quicksort(l, split+1, end)
  else:
    return

if __name__=="__main__":
  import sys
  l= x
  t1= time.time()
  start=0
  end=len(l)-1
  quicksort(l, start, end)
  import string
#  print string.join(map(str, l))
#  print l
  t2=time.time()
  f1=open("quick_sort.txt", "w")
  for i in x:
    print>>f1, i

  print "time taken by quick sort is:\n"
  print t2-t1

