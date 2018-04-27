import time

#x=[6,4,3,7,3,2,6,8,4,2,5,7,9,7,7,9]
#print x
f=open("data.txt", "r")
x=f.read().splitlines()
for i in range(len(x)):
 x[i]=int(x[i])
f.close()

t1=time.time()
for i in range(len(x)):
 least=i
 for j in range(i+1, len(x)):
  if x[j] < x[least]:
   least=j
 x[least], x[i]=x[i], x[least]
  
#print x
t2=time.time()
f1=open("selection_sort.txt", "w")
for i in x:
 print>>f1, i

print "time taken by selection sort is:\n"
print t2-t1
