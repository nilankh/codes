n=int(input())
arr=[int(i) for i in input().split()]
x=int(input())
def rec(arr,start,x):
    if start==len(arr):
        return
    if arr[start]==x:
        print(start,end=" ")
    rec(arr,start+1,x)

rec(arr,0,x)



