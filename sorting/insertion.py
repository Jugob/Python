import time

def inputdata():
 f=open("data.txt", "r")
 x=f.read().splitlines()
 for i in range(len(x)):
  x[i]=int(x[i])
 f.close()
 return x

def sort_numbers(s):
 for i in range(1, len(s)):
  val = s[i]
  j = i - 1
  while (j >= 0) and (s[j] > val):
    s[j+1] = s[j]
    j = j - 1
    s[j+1] = val
 return s


#define the insertion sort function
def insertionsort(l):
 for i in range(len(l)):
  j=i
  while j>0:
   if l[j]<l[j-1]:
    l[j], l[j-1]=l[j-1], l[j]
   j-=1
 return l
if __name__=='__main__':
#  x=[9,8,7,6,5,4,3,2,1]
  x=inputdata()
  t1=time.time()
  #res=insertionsort(x)
  res=sort_numbers(x)
  t2=time.time()
  print "time taken by insertion sort is:\n"
  print t2-t1

#f1=open("insertion_sort.txt", "w")
#for i in x:
# print>>f1, i


