'''
n=int(input())
arr=[int(x) for x in input().split()]
def sort012(arr,n):
    count0=0
    count1=0
    count2=0
    for i in range(0,n):
        if (arr[i]==0):
            count0=count0+1
        if (arr[i]==1):
            count1=count1+1
        if (arr[i]==2):
            count2=count2+1
    for i in range(0,count0):
        arr[i]=0
    for i in range(count0,(count0+count1)):
        arr[i]=1      
    for i in range((count0+count1),n):
        arr[i]=2
    return
def printarray(arr,n):
    for i in range(0,n):
        print (arr[i],end=' ')
    print()
n=len(arr)
sort012(arr,n)
printarray(arr,n)


'''
def sort012(arr):
    l = len(arr)
    i = 0
    nZ = 0
    nT = l - 1
    while(i <= nT):
        if(arr[i] == 0):
            arr[i],arr[nZ] = arr[nZ],arr[i]
            i = i + 1
            nZ = nZ + 1
        elif arr[i] == 2:
            arr[i],arr[nT] = arr[nT],arr[i]
            nT = nT - 1
        else:
            i = i + 1
            
n = int(input())
arr = [int(x) for x in input().split()]
sort012(arr)
for num in arr:
    print(num,end = ' ')
print()


