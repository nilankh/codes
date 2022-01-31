'''
def pushZerosToEnd(arr):
    length=len(arr)
    j=0
    for i in range(0,length):
        if(arr[i] == 0):
            continue
        arr[j]=arr[i]
        print("first", arr)
        j+=1
    while(j<n):
        arr[j]=0
        j+=1
        print("last",arr)
n=int(input())
arr=[int(x) for x in input().split()]
pushZerosToEnd(arr)
print(arr)
'''
def pushZerosToEnd(arr, n): 
    count = 0 
   
    for i in range(n): 
        if arr[i] != 0: 
           
            arr[count] = arr[i] 
            count+=1
      
    
    while count < n: 
        arr[count] = 0
        count += 1
n=int(input())
arr=[int(x) for x in input().split()]
n = len(arr) 
pushZerosToEnd(arr, n) 

print(*arr)
