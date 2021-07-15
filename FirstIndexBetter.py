def FirstIndexB(a,x,si):
    length=len(a)
    if si==length:
        return -1
    if a[si]==x:
        return si
    smallerListOutput=FirstIndexB(a,x,si+1)
    return smallerListOutput
a=[1,2,3,4,5,6,7,8,9]
print(FirstIndexB(a,7,0))
