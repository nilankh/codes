'''
def sort01(arr):
    length=len(arr)
    start=0
    end=length-1
    while(start<end):
        while(arr[start]==0 and start<end):
            start+=1
        while(arr[end]==1 and start<end):
            end-=1
        if(start<end):
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1

n=int(input())
arr=[int(x) for x in input().split()]
sort01(arr)
print(*arr) 
'''
def sort01(arr):
    length=len(arr)

    count=0

    for i in range(length):
        if(arr[i]==0):
            count+=1
    for i in range(count):
        print(0,end=' ')
    for j in range(length-count):
        print(1,end=' ')

n=int(input())
arr=[int(x) for x in input().split()]
sort01(arr)









