N=int(input("enter N"))
a=[]
for i in range(0,N):
  b=int(input())
  a.append(b)
k=int(input("enter k"))
if(k in a):
  print("yes")
else:
  print("no")
