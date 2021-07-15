import heapq
def time_required(lst, k):
    q=lst[k]
    heapq._heapify_max(lst)
    time=0
    while True:
        ele_max = heapq._heappop_max(lst)
        time+=1
        if ele_max==q:
            return time
# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=time_required(lst, k)
print(ans)



