#time complexity is O(logn)
def binarySearch(arr,element):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==element):
           return mid
        elif(arr[mid]<element):
           start=mid+1
        else:
           end=mid-1
    return -1
n=int(input())
arr=[int(x) for x in input().split()]
element=int(input())
index=binarySearch(arr,element)
print(index)
