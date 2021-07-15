##import heapq
##
##def kSmallest(arr, k):
##
##    heap = arr[:k]
##    heapq._heapify_max(heap)
##    #print(heap)
##    n = len(arr)
##    for i in range(k, n):
##        if heap[0] > arr[i]:
##            heapq._heapreplace_max(heap, arr[i])
##    return heap
##    
##arr = [10, 6, 7, 2, 3, 8, 9, 11, 1]
##k = 4
##elements = kSmallest(arr, k)
##for ele in elements:
##    print(ele, end = " ")
####
def checkBalanced(exp):
### Implement your code here
    s=[]
    for char in exp:
        if char in'({[':
            s.append(char)
        elif char is ')':
            if (not s or s[-1]!='('):
                return False
            s.pop()
        elif char is '}':
            if (not s or s[-1]!='{'):
                return False
            s.pop()
        elif char is ']':
            if (not s or s[-1]!='['):
                return False
            s.pop()
    if(not s):
        return True
    return False
        
    

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

