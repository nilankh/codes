#time complexity is O(n^2)
def bubbleSort(arr):
    length=len(arr)
    #i is for n-1 rounds
    for i in range(length-1):
        #j is for in each iteration you need to go till length-1-i position
        for j in range(length-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
n=int(input())
arr=[int(x) for x in input().split()]
bubbleSort(arr)
print(*arr)
#*arr likhnse list ki value print krayega
