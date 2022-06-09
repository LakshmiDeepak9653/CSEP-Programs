#compound Interest
from matplotlib import pyplot as pt
def compoundint(p,r,t):
    lst=[]
    x=[]
    for i in range(1,n+1):
        x.append(i)
        a=p*(1+(r/100))**(i*t)
        ci=a-p
        lst.append(ci)
    pt.plot(x,lst)
    return ci

p=int(input("Enter the principle"))
r=int(input("Enter the rate of interest"))
t=int(input("Enter the time"))
n=int(input("Enter the compound interset interval"))

print("compound interest is",compoundint(p,r,t))
