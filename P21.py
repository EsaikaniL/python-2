x1,y1=map(int,input("Enter !st line").split(' '))
x2,y2=map(int,input("Enter 2nd line").split(' '))
x3,y3=map(int,input("Enter 3rd line").split(' '))
if (x1==x2 and x2==x3) or(y1==y2 and y2==y3) or (abs(x1-x2)==abs(x2-x3) and abs(y1-y2)==abs(y2-y3)):
  print("yes")
else:
  print("no")
