def lastIndexB(a,x,si):
    length=len(a)
    if si==length:
        return -1
    smallerListOutput=lastIndexB(a,x,si+1)
    if smallerListOutput!=-1:
        return smallerListOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1
    
n=int(input())
a=[int(i) for i in input().split()]
x=int(input())
print(lastIndexB(a,x,0))
