import heapq
def checkMaxHeap(lst):
    arr = []
    for ele in lst:
        arr.append(ele)
    #print(arr)
    heapq._heapify_max(arr)
    print(arr)
    for i in range(len(lst)):
        #print(i)
        #print("lst", lst[i])
        if arr[i] != lst[i]:
            return False
    return True

n = int(input())
lst = [int(i) for i in input().split()]
print('true') if checkMaxHeap(lst) else print('false')
            
