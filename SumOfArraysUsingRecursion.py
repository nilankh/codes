def sumArray(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+sumArray(arr[1:])
    
n=int(input())
arr=[int(x) for x in input().split()]
print(sumArray(arr))
