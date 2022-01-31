'''
#another method
def reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
def Rotate(arr,d):
    length=len(arr)

    reverse(arr,0,length-1)
    reverse(arr,0,length-d-1)
    reverse(arr,length-d,length-1)

n=int(input())
arr=[int(x) for x in input().split()]
d=int(input())
Rotate(arr,d)
print(*arr)'''
'''
def Reverse(arr,start,end):
    while (start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def Rotate(arr,d):
    size=len(arr)
    
    Reverse(arr,0,size-1)
    Reverse(arr,0,size-d-1)
    Reverse(arr,size-d,size-1)
n= int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr,d)
print(*arr)'''


''' 3rd method'''
def Rotate(arr,d):
    length=len(arr)
    for i in range(d):
        temp=arr[0]
        for i in range(length-1):
            arr[i]=arr[i+1]
        arr[length-1]=temp
        
n=int(input())
arr=[int(x) for x in input().split()]
d=int(input())
Rotate(arr,d)
print(*arr)


##def Rotate(arr, d):
##    n = len(arr)
##    li=[]
##    for i in range(0,d):
##        li.append(arr[i])
##    
##    for i in range(0, n-d):
##        arr[i]=arr[i+d]
##    for i in range(0, d):
##        
##        arr[n - d + i]=li[i]
##n=int(input())
##arr=list(int(i) for i in input().strip().split(' '))
##d=int(input())
##Rotate(arr, d)
##print(*arr)




    
