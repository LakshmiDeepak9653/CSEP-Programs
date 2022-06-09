#Binary Search in recursive
def binsearch(lst,l,h,key):
    if h>=l:
        mid=(h+l)//2
        if(lst[mid]==key):
            return mid
        elif(lst[mid]>key):
            return binsearch(lst,l,mid -1,key)
        else:
            return binsearch(lst,mid +1,h,key)
    else:
        return 0
    
    
    
    
    
    
lst=[1,2,3,56,78,81,90]
print("THe list is ",lst)
key=int(input("Enter search element"))

output=binsearch(lst,0,len(lst)-1,key)

if output !=0:
    print("Element found in index",output)
else:
    print("Element not found")
