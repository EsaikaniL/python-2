
a=list(input())
b=len(a)-1
for i in range(0,b,2):
    a[i],a[i+1]=a[i+1],a[i]
print("".join(str(x) for x in a))
