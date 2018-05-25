def power(n):
    n = n/2
    if n == 2:
        print("s")
    elif n > 2:
        return power(n)
    else:
        print("no") 
s=int(input("enter a numbers"))
power(s)
