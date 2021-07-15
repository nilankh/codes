def equilibriumIndex(arr):
    ts=0
    i=0
    while i<len(arr):
        ts+=arr[i]
        i=i+1
    left_sum=0
    index=0
    while index<len(arr):
        right_sum=ts-left_sum-arr[index]
        if(right_sum==left_sum):
            return index
        left_sum=left_sum+arr[index]
        index=index+1
    return -1
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
