#time complexity is O(n^2)
def insertionSort(arr):
    length=len(arr)
    for i in range(1,length):
        #print("ye i", i)
        j=i-1
        temp=arr[i]
        #shifting elements till this condition holds
        while(j>=0 and arr[j]>temp):
            #print("before hahahha", arr)
            arr[j+1]=arr[j]
            #print("after hahahha", arr)
            j=j-1
        arr[j+1]=temp
        #print("chala", arr)
n=int(input())
arr=[int(x) for x in input().split()]
insertionSort(arr)
print(arr)
'''
def rotate(arr):
    length = len(arr)
    for i in range(0,length - 1):
        if(arr[i] > arr[i + 1]):
           return i + 1
    return 0

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(rotate(arr))
'''
