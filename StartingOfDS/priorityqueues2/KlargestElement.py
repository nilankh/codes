
import heapq
def kthLargest(lst, k):
    minHeap = lst[:k]
    #print(minHeap)
    heapq.heapify(minHeap)
    print(minHeap)
    n = len(lst)
    for i in range(k, n):
        if lst[i] > minHeap[0]:
            heapq.heapreplace(minHeap, lst[i])
            print(minHeap)
    return minHeap[0]

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)


#second method
##import heapq
##def kthLargest(lst, k):
##     heapq._heapify_max(lst)
##     #print(lst)
##     #print(lst[:k])
##     for i in range(k):
##         
##         a=heapq._heappop_max(lst)
##         #print(lst)
##         #print(a)
##     return a
##    
##
### Main Code
##n=int(input())
##lst=list(int(i) for i in input().strip().split(' '))
##k=int(input())
##ans=kthLargest(lst, k)
##print(ans)
##



