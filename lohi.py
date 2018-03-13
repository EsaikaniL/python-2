a=[]
n=int(input("Enter n val"))
for i in range(0,n):
  b=int(input())
  a.append(b)
a.sort()
print(a[0],a[n-1])
