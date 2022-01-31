def swap_alternate(arr):
    n = len(arr)
    for i in range(0,n,2):
        if i+1 < n:
            arr[i], arr[i+1] = arr[i+1], arr[i]

n = int(input())
arr = [int(i) for i in input().split()]
swap_alternate(arr)
for ele in arr:
    print(ele, end = ' ')
