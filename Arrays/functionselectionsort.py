#time complexity is O(n^2)
def selectionSort(arr):
    length=len(arr)
    #put the correct element at ith position
    for i in range(length-1):
        minIndex=i
        #calculating the index of minimum element for this iteration
        for j in range(i+1,length):
            if(arr[j]<arr[minIndex]):
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]
    #return arr
        

        
n=int(input())
arr=[int(x) for x in input().split()]

selectionSort(arr)
print(arr)
