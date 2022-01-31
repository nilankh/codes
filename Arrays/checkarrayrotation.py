def checkArrayRotation(arr):
    minval=min(arr)
    count=0
    for i in arr:
        if i==minval:
            break
        else:
            count=count+1
    print(count)
n=int(input())
arr=[int(x) for x in input().split()]
checkArrayRotation(arr)
# above code will fail for 3 3 3 4 3
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
