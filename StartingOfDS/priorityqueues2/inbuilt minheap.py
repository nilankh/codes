import heapq

li = [1, 5, 4, 8, 7, 9, 11]
##li = [10,5,11,2,3,7,12,1,6]
heapq.heapify(li)
print(li)

heapq.heappush(li, 2)
print(li)


print(heapq.heappop(li))
#remove minimum element 

print(li)

heapq.heapreplace(li, 6)
print(li)

heapq.heapreplace(li, 10)
print(li)
