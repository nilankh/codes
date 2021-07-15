def firstIndex(a,x):
    length=len(a)
    if length==0:
        return -1
    if a[0]==x:
        return 0
    smallerList=a[1:]
    smallerListOutput=firstIndex(smallerList,x)
    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1 
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
a=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(a, x))
