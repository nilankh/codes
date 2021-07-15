import heapq
def kLargest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for i in range(k, len(arr), 1):
        if arr[i] > heap[0]:
            heapq.heapreplace(heap, arr[i])
    return heap

n = int(input())
arr = [int(i) for i in input().split()]
k = int(input())
ans = kLargest(arr, k)
for ele in ans:
    print(ele)
