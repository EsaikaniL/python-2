def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def modulus(n1,n2):
    return n1%n2
    
print("select operation")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.division")
print("5.modulus")
print("6.square")
choice=int(input("enter your choice"))
n1=int(input("enter first num")) 
n2=int(input("enter second num")) 
if (choice==1):
    print(add(n1,n2))
elif(choice==2):
    print(subtract(n1,n2))
elif(choice==3):
    print(multiply(n1,n2))
elif(choice==4):
    if(n1 or n2==0):
        print("infinity")
    else:
        print(division(n1,n1))
elif(choice==5):
    if(n1 or n2==float):
    print(
    )
else:
    print(float)
    print(modulus(n1,n2))
else:
    print("invalid")
