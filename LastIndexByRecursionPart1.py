def LastIndex(a,x):
    length=len(a)
    if length==0:
        return -1
    smallerList=a[1:]
    smallerListOutput=LastIndex(smallerList,x)
    if smallerListOutput!=-1:
        return smallerListOutput+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1
n=int(input())
a=[int(i) for i in input().split()]
x=int(input())
print(LastIndex(a,x))
