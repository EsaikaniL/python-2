n=input('enter size')
a=[]
for i in range(n):
  b=int(input("enter number"))
  a.append(b)
  a.sort(reverse=True)
m=input('enter size')
p=[]
for i in range(m):
  q=int(input('enter number'))
  p.append(q)
if(a==p):
  print('yes')
else:
  print('no')
