import math
a,b=map(int,input().split(' '))
n1=a*b
if math.sqrt(n1)==int( math.sqrt(n1)):
    print ("Yes")
else:
    print ("No")
