import math
arry=[5,9,10,20,35,50,60,70,75]

def BSearch(a,x,low,high):
    if low<=high:
        mid=math.floor((low+high)/2)  
        if a[mid]==x :
            print(a[mid])
        if x<a[mid]:
            BSearch(a,x,low,mid-1)
        elif x>a[mid]:
            BSearch(a,x,mid+1,high)
        
    if low>high:
        return -1

#################################################################

x=60
low=0
high=len(arry) -1


BSearch(arry,x,low,high)

