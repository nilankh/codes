def BinarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return BinarySearch(a,x,si,mid-1)
    else:
        return BinarySearch(a,x,mid+1,ei)
n=int(input())
a=[int(k) for k in input().split()]
x=int(input())
si=0
ei=len(a)-1
index=BinarySearch(a,x,si,ei)
print(index)



