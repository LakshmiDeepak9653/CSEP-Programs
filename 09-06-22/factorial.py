#Factorial using Recursion

def fac(n):
    if(n==1 or n==0):
        return 1
    else:
        x=n*fac(n-1)
        return x
key=int(input("Enter the number"))
print("factorial of ",key,"is",fac(key))
